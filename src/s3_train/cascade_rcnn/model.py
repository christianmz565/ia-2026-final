"""Cascade R-CNN Object Detection Model with ConvNeXt Backbone and PAFPN Neck.

Architectural details:
- Backbone: ConvNeXt (Tiny or Small) initialized with COCO/ImageNet transfer learning weights.
- Neck: Path Aggregation Feature Pyramid Network (PAFPN) with top-down and bottom-up feature fusion.
- RPN: Region Proposal Network generating candidate bounding box proposals across multi-scale features.
- Detector Head: 3-stage Cascade R-CNN head with increasing IoU thresholds (0.5, 0.6, 0.7) for box refinement and classification.
"""

from typing import cast

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision.models.detection._utils import BoxCoder
from torchvision.models.detection.anchor_utils import AnchorGenerator
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor, TwoMLPHead
from torchvision.models.detection.rpn import RegionProposalNetwork, RPNHead
from torchvision.models.detection.transform import GeneralizedRCNNTransform
from torchvision.ops import MultiScaleRoIAlign
from torchvision.ops import boxes as box_ops


class ConvNeXtFeatureExtractor(nn.Module):
    """ConvNeXt backbone wrapper extracting multi-scale feature maps C2, C3, C4, C5."""

    def __init__(self, variant: str = "convnext_tiny", pretrained: bool = True):
        super().__init__()
        self.variant = variant
        if variant == "convnext_tiny":
            weights = torchvision.models.ConvNeXt_Tiny_Weights.DEFAULT if pretrained else None
            model = torchvision.models.convnext_tiny(weights=weights)
            self.in_channels = [96, 192, 384, 768]
        elif variant == "convnext_small":
            weights = torchvision.models.ConvNeXt_Small_Weights.DEFAULT if pretrained else None
            model = torchvision.models.convnext_small(weights=weights)
            self.in_channels = [96, 192, 384, 768]
        else:
            raise ValueError(f"Unsupported ConvNeXt variant: {variant}")

        # ConvNeXt features stages
        self.stage0 = model.features[0]  # Stem: 4x downsampling
        self.stage1 = model.features[1]  # Stage 1: C2 (96 ch, stride 4)
        self.stage2 = model.features[2:4]  # Downsample + Stage 2: C3 (192 ch, stride 8)
        self.stage3 = model.features[4:6]  # Downsample + Stage 3: C4 (384 ch, stride 16)
        self.stage4 = model.features[6:8]  # Downsample + Stage 4: C5 (768 ch, stride 32)

    def forward(self, x: torch.Tensor) -> dict[str, torch.Tensor]:
        x0 = self.stage0(x)
        c2 = self.stage1(x0)
        c3 = self.stage2(c2)
        c4 = self.stage3(c3)
        c5 = self.stage4(c4)
        return {"0": c2, "1": c3, "2": c4, "3": c5}


class PAFPN(nn.Module):
    """Path Aggregation Feature Pyramid Network (PAFPN).

    Constructs top-down FPN feature maps (P2..P5) and adds bottom-up path augmentation (N2..N6).
    """

    def __init__(self, in_channels_list: list[int], out_channels: int = 256):
        super().__init__()
        self.out_channels = out_channels

        # Top-down 1x1 lateral convolutions
        self.lateral_convs = nn.ModuleList(
            [nn.Conv2d(in_ch, out_channels, kernel_size=1) for in_ch in in_channels_list]
        )
        # FPN 3x3 smoothing convolutions
        self.fpn_convs = nn.ModuleList(
            [nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1) for _ in in_channels_list]
        )
        # Bottom-up PAFPN 3x3 stride-2 downsampling convolutions
        self.pafpn_convs = nn.ModuleList(
            [
                nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=2, padding=1)
                for _ in range(len(in_channels_list) - 1)
            ]
        )
        # Extra 3x3 stride-2 maxpool / conv for stage 6 (RPN)
        self.extra_pooling = nn.MaxPool2d(kernel_size=1, stride=2)

    def forward(self, inputs: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:
        feats = [inputs[str(i)] for i in range(len(inputs))]

        # 1. Top-down FPN path
        laterals = [lateral_conv(feats[i]) for i, lateral_conv in enumerate(self.lateral_convs)]

        for i in range(len(laterals) - 1, 0, -1):
            prev_shape = laterals[i - 1].shape[2:]
            laterals[i - 1] = laterals[i - 1] + F.interpolate(laterals[i], size=prev_shape, mode="nearest")

        fpn_outs = [self.fpn_convs[i](laterals[i]) for i in range(len(laterals))]

        # 2. Bottom-up path augmentation (PAFPN)
        pafpn_outs = [fpn_outs[0]]
        for i in range(len(fpn_outs) - 1):
            downsampled = self.pafpn_convs[i](pafpn_outs[-1])
            pafpn_outs.append(downsampled + fpn_outs[i + 1])

        # Add extra scale for RPN
        pafpn_outs.append(self.extra_pooling(pafpn_outs[-1]))

        out_dict = {str(i): pafpn_outs[i] for i in range(len(pafpn_outs) - 1)}
        out_dict["pool"] = pafpn_outs[-1]
        return out_dict


class CascadeRCNNStage(nn.Module):
    """Single stage of Cascade R-CNN detector head."""

    iou_threshold: float

    def __init__(
        self,
        in_channels: int,
        representation_size: int,
        num_classes: int,
        iou_threshold: float,
    ):
        super().__init__()
        self.iou_threshold = iou_threshold
        self.box_head = TwoMLPHead(in_channels * 7 * 7, representation_size)
        self.box_predictor = FastRCNNPredictor(representation_size, num_classes)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        box_features = self.box_head(x)
        class_logits, box_regression = self.box_predictor(box_features)
        return class_logits, box_regression


class CascadeRCNN(nn.Module):
    """Full Cascade R-CNN Object Detector.

    Combines ConvNeXt + PAFPN + RPN + 3-Stage Cascade RoI Heads.
    """

    def __init__(
        self,
        num_classes: int = 9,  # 8 defect classes + 1 background class
        backbone_variant: str = "convnext_tiny",
        pretrained: bool = True,
        out_channels: int = 256,
        cascade_iou_thresholds: list[float] | None = None,
    ):
        super().__init__()
        self.cascade_iou_thresholds = cascade_iou_thresholds or [0.5, 0.6, 0.7]
        self.num_classes = num_classes
        self.backbone_variant = backbone_variant

        # 1. ConvNeXt Backbone & PAFPN Neck
        self.backbone = ConvNeXtFeatureExtractor(variant=backbone_variant, pretrained=pretrained)
        self.neck = PAFPN(in_channels_list=self.backbone.in_channels, out_channels=out_channels)

        # 2. Anchor Generator & RPN
        anchor_sizes = ((32,), (64,), (128,), (256,), (512,))
        aspect_ratios = ((0.5, 1.0, 2.0),) * len(anchor_sizes)
        self.anchor_generator = AnchorGenerator(anchor_sizes, aspect_ratios)

        rpn_head = RPNHead(out_channels, self.anchor_generator.num_anchors_per_location()[0])
        self.rpn = RegionProposalNetwork(
            self.anchor_generator,
            rpn_head,
            fg_iou_thresh=0.7,
            bg_iou_thresh=0.3,
            batch_size_per_image=256,
            positive_fraction=0.5,
            pre_nms_top_n={"training": 2000, "testing": 1000},
            post_nms_top_n={"training": 2000, "testing": 1000},
            nms_thresh=0.7,
        )

        # 3. Multi-Scale RoI Align
        self.box_roi_pool = MultiScaleRoIAlign(featmap_names=["0", "1", "2", "3"], output_size=7, sampling_ratio=2)

        # 4. Cascade Stages (3 stages with IoU thresholds 0.5, 0.6, 0.7)
        self.cascade_stages = nn.ModuleList(
            [
                CascadeRCNNStage(
                    in_channels=out_channels,
                    representation_size=1024,
                    num_classes=num_classes,
                    iou_threshold=thresh,
                )
                for thresh in self.cascade_iou_thresholds
            ]
        )

        self.box_coder = BoxCoder(weights=(10.0, 10.0, 5.0, 5.0))

        # Transform for standard image normalization check
        self.transform = GeneralizedRCNNTransform(
            min_size=800,
            max_size=1333,
            image_mean=[0.485, 0.456, 0.406],
            image_std=[0.229, 0.224, 0.225],
        )

    def forward(
        self,
        images: list[torch.Tensor],
        targets: list[dict[str, torch.Tensor]] | None = None,
    ) -> dict[str, torch.Tensor] | list[dict[str, torch.Tensor]]:
        """Forward pass for training or inference.

        If targets are provided, computes losses.
        Otherwise, returns bounding box predictions.
        """
        original_image_sizes: list[tuple[int, int]] = []
        for img in images:
            val = img.shape[-2:]
            original_image_sizes.append((val[0], val[1]))

        # Extract features (Pad images to max H, W multiple of 32 without resizing)
        if isinstance(images, list):
            max_h = max(img.shape[-2] for img in images)
            max_w = max(img.shape[-1] for img in images)
            pad_h = (max_h + 31) // 32 * 32
            pad_w = (max_w + 31) // 32 * 32

            padded_list = []
            for img in images:
                c, h, w = img.shape
                padded = torch.zeros((c, pad_h, pad_w), dtype=img.dtype, device=img.device)
                padded[:, :h, :w] = img
                padded_list.append(padded)
            image_tensors = torch.stack(padded_list, dim=0)
        else:
            image_tensors = images

        conv_feats = self.backbone(image_tensors)
        pafpn_feats = self.neck(conv_feats)

        image_shapes: list[tuple[int, int]] = [(int(s[0]), int(s[1])) for s in (img.shape[-2:] for img in images)]
        image_list_obj = torchvision.models.detection.image_list.ImageList(  # pyright: ignore[reportAttributeAccessIssue]
            image_tensors, image_shapes
        )

        # RPN proposals
        proposals, rpn_losses = self.rpn(image_list_obj, pafpn_feats, targets)

        if self.training:
            assert targets is not None
            losses = dict(rpn_losses)

            curr_proposals = proposals
            for stage_idx, stage in enumerate(self.cascade_stages):
                # RoI Align
                box_features = self.box_roi_pool(pafpn_feats, curr_proposals, image_shapes)
                class_logits, box_regression = stage(box_features)

                # Match targets for stage IoU threshold
                matched_idxs, labels = self._select_training_samples(
                    curr_proposals, targets, cast(float, stage.iou_threshold)
                )

                # Compute stage classification and regression losses
                loss_cls, loss_reg = self._compute_stage_loss(
                    class_logits, box_regression, curr_proposals, targets, labels
                )

                losses[f"loss_classifier_stage_{stage_idx + 1}"] = loss_cls
                losses[f"loss_box_reg_stage_{stage_idx + 1}"] = loss_reg

                # Refine proposals for next cascade stage
                if stage_idx < len(self.cascade_stages) - 1:
                    curr_proposals = self._refine_proposals(curr_proposals, box_regression, image_shapes)

            return losses

        else:
            # Inference pass across cascade stages
            curr_proposals = proposals
            final_class_logits = None
            final_box_regression = None

            for stage_idx, stage in enumerate(self.cascade_stages):
                box_features = self.box_roi_pool(pafpn_feats, curr_proposals, image_shapes)
                class_logits, box_regression = stage(box_features)
                final_class_logits = class_logits
                final_box_regression = box_regression

                if stage_idx < len(self.cascade_stages) - 1:
                    curr_proposals = self._refine_proposals(curr_proposals, box_regression, image_shapes)

            # Post-process predictions
            assert final_class_logits is not None
            assert final_box_regression is not None
            result = self._post_process(
                final_class_logits,
                final_box_regression,
                curr_proposals,
                original_image_sizes,
            )
            return result

    def _select_training_samples(
        self,
        proposals: list[torch.Tensor],
        targets: list[dict[str, torch.Tensor]],
        iou_thresh: float,
    ) -> tuple[list[torch.Tensor], list[torch.Tensor]]:
        labels = []
        matched_idxs = []
        for props, target in zip(proposals, targets, strict=False):
            gt_boxes = target["boxes"]
            gt_labels = target["labels"]
            if gt_boxes.numel() == 0:
                labels.append(torch.zeros((props.shape[0],), dtype=torch.int64, device=props.device))
                matched_idxs.append(torch.zeros((props.shape[0],), dtype=torch.int64, device=props.device))
                continue

            match_quality_matrix = box_ops.box_iou(gt_boxes, props)
            matched_vals, matches = match_quality_matrix.max(dim=0)

            # Assign labels based on stage IoU threshold
            matched_labels = gt_labels[matches].clone()
            matched_labels[matched_vals < iou_thresh] = 0  # Background

            labels.append(matched_labels)
            matched_idxs.append(matches)

        return matched_idxs, labels

    def _compute_stage_loss(
        self,
        class_logits: torch.Tensor,
        box_regression: torch.Tensor,
        proposals: list[torch.Tensor],
        targets: list[dict[str, torch.Tensor]],
        labels: list[torch.Tensor],
    ) -> tuple[torch.Tensor, torch.Tensor]:
        concat_labels = torch.cat(labels, dim=0)
        loss_cls = F.cross_entropy(class_logits, concat_labels)

        # Box regression loss on positive samples only
        pos_inds = torch.where(concat_labels > 0)[0]
        if pos_inds.numel() == 0:
            loss_reg = class_logits.sum() * 0.0
        else:
            sampled_pos_labels = concat_labels[pos_inds]
            box_regression = box_regression.reshape(class_logits.shape[0], -1, 4)
            pos_box_regression = box_regression[pos_inds, sampled_pos_labels]

            # Targets
            concat_proposals = torch.cat(proposals, dim=0)
            pos_proposals = concat_proposals[pos_inds]

            gt_boxes_list = []
            for target in targets:
                gt_boxes_list.append(target["boxes"])

            # Map positive proposal targets
            target_boxes_list = []
            offset = 0
            for props, target, lbls in zip(proposals, targets, labels, strict=False):
                n_props = props.shape[0]
                stage_pos = torch.where(lbls > 0)[0]
                if stage_pos.numel() > 0 and target["boxes"].numel() > 0:
                    ious = box_ops.box_iou(target["boxes"], props[stage_pos])
                    _, best_gt = ious.max(dim=0)
                    target_boxes_list.append(target["boxes"][best_gt])
                offset += n_props

            if len(target_boxes_list) > 0:
                pos_target_boxes = torch.cat(target_boxes_list, dim=0)
                target_deltas = self.box_coder.encode([pos_proposals], [pos_target_boxes])[0]
                loss_reg = F.smooth_l1_loss(pos_box_regression, target_deltas, beta=1.0 / 9.0, reduction="sum") / max(
                    1, concat_labels.numel()
                )
            else:
                loss_reg = class_logits.sum() * 0.0

        return loss_cls, loss_reg

    def _refine_proposals(
        self,
        proposals: list[torch.Tensor],
        box_regression: torch.Tensor,
        image_shapes: list[tuple[int, int]],
    ) -> list[torch.Tensor]:
        boxes_per_image = [len(p) for p in proposals]
        box_regression = box_regression.reshape(-1, self.num_classes, 4)
        # Use mean class delta or class 1 delta for proposal refinement
        mean_deltas = box_regression[:, 1:, :].mean(dim=1)

        split_deltas = mean_deltas.split(boxes_per_image, dim=0)
        refined_proposals = []
        for props, deltas, shape in zip(proposals, split_deltas, image_shapes, strict=False):
            refined = self.box_coder.decode(deltas.unsqueeze(0), [props])[0]
            refined = box_ops.clip_boxes_to_image(refined, shape)
            refined_proposals.append(refined)
        return refined_proposals

    def _post_process(
        self,
        class_logits: torch.Tensor,
        box_regression: torch.Tensor,
        proposals: list[torch.Tensor],
        image_shapes: list[tuple[int, int]],
    ) -> list[dict[str, torch.Tensor]]:
        num_classes = class_logits.shape[-1]
        device = class_logits.device
        pred_scores = F.softmax(class_logits, dim=-1)
        box_regression = box_regression.reshape(-1, num_classes, 4)

        boxes_per_image = [len(p) for p in proposals]
        split_scores = pred_scores.split(boxes_per_image, dim=0)
        split_boxes = box_regression.split(boxes_per_image, dim=0)

        results: list[dict[str, torch.Tensor]] = []
        score_thresh = 0.05
        nms_thresh = 0.5
        detections_per_img = 100

        for _i, (scores, boxes, props, shape) in enumerate(
            zip(split_scores, split_boxes, proposals, image_shapes, strict=False)
        ):
            decoded_boxes = self.box_coder.decode(boxes, [props] * num_classes)
            # Clip boxes
            decoded_boxes = box_ops.clip_boxes_to_image(decoded_boxes, shape)

            # Keep foreground classes
            labels = torch.arange(num_classes, device=device)
            labels = labels.view(1, -1).expand_as(scores)

            # Drop background (label 0)
            scores = scores[:, 1:]
            boxes = decoded_boxes[:, 1:]
            labels = labels[:, 1:]

            # Batch NMS across classes
            boxes = boxes.reshape(-1, 4)
            scores = scores.reshape(-1)
            labels = labels.reshape(-1)

            # Filter low scores
            keep = torch.where(scores > score_thresh)[0]
            boxes, scores, labels = boxes[keep], scores[keep], labels[keep]

            # NMS per class
            keep = box_ops.batched_nms(boxes, scores, labels, nms_thresh)
            keep = keep[:detections_per_img]

            results.append(
                {
                    "boxes": boxes[keep],
                    "scores": scores[keep],
                    "labels": labels[keep],
                }
            )

        return results
