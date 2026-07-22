"""MMDetection Config Builder module.

Constructs MMDetection 3.x Config for Cascade R-CNN + ConvNeXt + PAFPN.
Enforces strict baseline rules (Native image resolution, No augmentations, AMP FP16).
"""

from mmengine.config import Config

from src.s3_train.cascade_rcnn.config import PipelineConfig


def build_mmdet_config(config: PipelineConfig) -> Config:
    """Build MMDetection 3.x Config object from PipelineConfig."""
    num_classes = config.dataset.num_classes
    work_dir = str(config.dataset.output_dir)

    # Class names mapping
    classes = tuple(config.dataset.class_names)

    # Data pipeline for native resolution baseline (No Resize, No Augmentation)
    train_pipeline = [
        {"type": "LoadImageFromFile", "backend_args": None},
        {"type": "LoadAnnotations", "with_bbox": True},
        {"type": "PackDetInputs"},
    ]

    test_pipeline = [
        {"type": "LoadImageFromFile", "backend_args": None},
        {"type": "LoadAnnotations", "with_bbox": True},
        {"type": "PackDetInputs"},
    ]

    # Model Dictionary: Cascade R-CNN + ConvNeXt + PAFPN
    model_cfg = {
        "type": "CascadeRCNN",
        "data_preprocessor": {
            "type": "DetDataPreprocessor",
            "mean": [123.675, 116.28, 103.53],
            "std": [58.395, 57.12, 57.375],
            "bgr_to_rgb": True,
            "pad_size_divisor": 32,
        },
        "backbone": {
            "type": "mmpretrain.ConvNeXt",
            "arch": "tiny" if config.model.backbone_variant == "convnext_tiny" else "small",
            "out_indices": (0, 1, 2, 3),
            "drop_path_rate": 0.1,
            "layer_scale_init_value": 1e-6,
            "gap_before_final_norm": False,
            "init_cfg": {
                "type": "Pretrained",
                "checkpoint": "https://download.openmmlab.com/mmclassification/v0/convnext/convnext-tiny_3rdparty_32xb128-no_aug_in1k_20220301-713e54b6.pth"
                if config.model.backbone_variant == "convnext_tiny"
                else "https://download.openmmlab.com/mmclassification/v0/convnext/convnext-small_3rdparty_32xb128-noaug_in1k_20220301-70bf8122.pth",
                "prefix": "backbone.",
            }
            if config.model.pretrained
            else None,
        },
        "neck": {
            "type": "PAFPN",
            "in_channels": config.model.in_channels,
            "out_channels": config.model.out_channels,
            "num_outs": 5,
        },
        "rpn_head": {
            "type": "RPNHead",
            "in_channels": config.model.out_channels,
            "feat_channels": config.model.out_channels,
            "anchor_generator": {
                "type": "AnchorGenerator",
                "scales": [8],
                "ratios": config.model.rpn_anchor_ratios,
                "strides": [4, 8, 16, 32, 64],
            },
            "bbox_coder": {
                "type": "DeltaXYWHBBoxCoder",
                "target_means": [0.0, 0.0, 0.0, 0.0],
                "target_stds": [0.1, 0.1, 0.2, 0.2],
            },
            "loss_cls": {"type": "CrossEntropyLoss", "use_sigmoid": True, "loss_weight": 1.0},
            "loss_bbox": {"type": "SmoothL1Loss", "beta": 1.0 / 9.0, "loss_weight": 1.0},
        },
        "roi_head": {
            "type": "CascadeRoIHead",
            "num_stages": config.model.num_cascade_stages,
            "stage_loss_weights": [1.0, 0.5, 0.25],
            "bbox_roi_extractor": {
                "type": "SingleRoIExtractor",
                "roi_layer": {"type": "RoIAlign", "output_size": 7, "sampling_ratio": 0},
                "out_channels": config.model.out_channels,
                "featmap_strides": [4, 8, 16, 32],
            },
            "bbox_head": [
                {
                    "type": "Shared2FCBBoxHead",
                    "in_channels": config.model.out_channels,
                    "fc_out_channels": 1024,
                    "roi_feat_size": 7,
                    "num_classes": num_classes,
                    "bbox_coder": {
                        "type": "DeltaXYWHBBoxCoder",
                        "target_means": [0.0, 0.0, 0.0, 0.0],
                        "target_stds": [0.1, 0.1, 0.2, 0.2],
                    },
                    "reg_class_agnostic": True,
                    "loss_cls": {
                        "type": "CrossEntropyLoss",
                        "use_sigmoid": False,
                        "loss_weight": 1.0,
                    },
                    "loss_bbox": {"type": "SmoothL1Loss", "beta": 1.0, "loss_weight": 1.0},
                },
                {
                    "type": "Shared2FCBBoxHead",
                    "in_channels": config.model.out_channels,
                    "fc_out_channels": 1024,
                    "roi_feat_size": 7,
                    "num_classes": num_classes,
                    "bbox_coder": {
                        "type": "DeltaXYWHBBoxCoder",
                        "target_means": [0.0, 0.0, 0.0, 0.0],
                        "target_stds": [0.05, 0.05, 0.1, 0.1],
                    },
                    "reg_class_agnostic": True,
                    "loss_cls": {
                        "type": "CrossEntropyLoss",
                        "use_sigmoid": False,
                        "loss_weight": 1.0,
                    },
                    "loss_bbox": {"type": "SmoothL1Loss", "beta": 1.0, "loss_weight": 1.0},
                },
                {
                    "type": "Shared2FCBBoxHead",
                    "in_channels": config.model.out_channels,
                    "fc_out_channels": 1024,
                    "roi_feat_size": 7,
                    "num_classes": num_classes,
                    "bbox_coder": {
                        "type": "DeltaXYWHBBoxCoder",
                        "target_means": [0.0, 0.0, 0.0, 0.0],
                        "target_stds": [0.033, 0.033, 0.067, 0.067],
                    },
                    "reg_class_agnostic": True,
                    "loss_cls": {
                        "type": "CrossEntropyLoss",
                        "use_sigmoid": False,
                        "loss_weight": 1.0,
                    },
                    "loss_bbox": {"type": "SmoothL1Loss", "beta": 1.0, "loss_weight": 1.0},
                },
            ],
        },
        "train_cfg": {
            "rpn": {
                "assigner": {
                    "type": "MaxIoUAssigner",
                    "pos_iou_thr": 0.7,
                    "neg_iou_thr": 0.3,
                    "min_pos_iou": 0.3,
                    "match_low_quality": True,
                    "ignore_iof_thr": -1,
                },
                "sampler": {
                    "type": "RandomSampler",
                    "num": 256,
                    "pos_fraction": 0.5,
                    "neg_pos_ub": -1,
                    "add_gt_as_proposals": False,
                },
                "allowed_border": 0,
                "pos_weight": -1,
                "debug": False,
            },
            "rpn_proposal": {
                "nms_pre": 2000,
                "max_per_img": 2000,
                "nms": {"type": "nms", "iou_threshold": 0.7},
                "min_bbox_size": 0,
            },
            "rcnn": [
                {
                    "assigner": {
                        "type": "MaxIoUAssigner",
                        "pos_iou_thr": config.model.cascade_iou_thresholds[0],
                        "neg_iou_thr": config.model.cascade_iou_thresholds[0],
                        "min_pos_iou": config.model.cascade_iou_thresholds[0],
                        "match_low_quality": False,
                        "ignore_iof_thr": -1,
                    },
                    "sampler": {
                        "type": "RandomSampler",
                        "num": 512,
                        "pos_fraction": 0.25,
                        "neg_pos_ub": -1,
                        "add_gt_as_proposals": True,
                    },
                    "pos_weight": -1,
                    "debug": False,
                },
                {
                    "assigner": {
                        "type": "MaxIoUAssigner",
                        "pos_iou_thr": config.model.cascade_iou_thresholds[1],
                        "neg_iou_thr": config.model.cascade_iou_thresholds[1],
                        "min_pos_iou": config.model.cascade_iou_thresholds[1],
                        "match_low_quality": False,
                        "ignore_iof_thr": -1,
                    },
                    "sampler": {
                        "type": "RandomSampler",
                        "num": 512,
                        "pos_fraction": 0.25,
                        "neg_pos_ub": -1,
                        "add_gt_as_proposals": True,
                    },
                    "pos_weight": -1,
                    "debug": False,
                },
                {
                    "assigner": {
                        "type": "MaxIoUAssigner",
                        "pos_iou_thr": config.model.cascade_iou_thresholds[2],
                        "neg_iou_thr": config.model.cascade_iou_thresholds[2],
                        "min_pos_iou": config.model.cascade_iou_thresholds[2],
                        "match_low_quality": False,
                        "ignore_iof_thr": -1,
                    },
                    "sampler": {
                        "type": "RandomSampler",
                        "num": 512,
                        "pos_fraction": 0.25,
                        "neg_pos_ub": -1,
                        "add_gt_as_proposals": True,
                    },
                    "pos_weight": -1,
                    "debug": False,
                },
            ],
        },
        "test_cfg": {
            "rpn": {
                "nms_pre": 1000,
                "max_per_img": 1000,
                "nms": {"type": "nms", "iou_threshold": 0.7},
                "min_bbox_size": 0,
            },
            "rcnn": {
                "score_thr": 0.05,
                "nms": {"type": "nms", "iou_threshold": 0.5},
                "max_per_img": 100,
            },
        },
    }

    # Datasets
    data_root = str(config.dataset.data_dir)
    train_dataloader = {
        "batch_size": config.training.batch_size,
        "num_workers": config.training.num_workers,
        "persistent_workers": config.training.num_workers > 0,
        "sampler": {"type": "DefaultSampler", "shuffle": True},
        "dataset": {
            "type": "CocoDataset",
            "data_root": data_root,
            "ann_file": str(config.dataset.train_json),
            "data_prefix": {"img": ""},
            "filter_cfg": {"filter_empty_gt": True, "min_size": 32},
            "pipeline": train_pipeline,
            "metainfo": {"classes": classes},
        },
    }

    val_dataloader = {
        "batch_size": config.training.batch_size,
        "num_workers": config.training.num_workers,
        "persistent_workers": False,
        "drop_last": False,
        "sampler": {"type": "DefaultSampler", "shuffle": False},
        "dataset": {
            "type": "CocoDataset",
            "data_root": data_root,
            "ann_file": str(config.dataset.val_json),
            "data_prefix": {"img": ""},
            "test_mode": True,
            "pipeline": test_pipeline,
            "metainfo": {"classes": classes},
        },
    }

    val_evaluator = {
        "type": "CocoMetric",
        "ann_file": str(config.dataset.val_json),
        "metric": "bbox",
        "format_only": False,
        "classwise": True,
    }

    # Optimization & AMP
    optim_wrapper = {
        "type": "AmpOptimWrapper" if config.training.amp_enabled else "OptimWrapper",
        "optimizer": {
            "type": "AdamW",
            "lr": config.training.lr,
            "weight_decay": config.training.weight_decay,
        },
        "paramwise_cfg": {
            "custom_keys": {
                "absolute_pos_embed": {"decay_mult": 0.0},
                "relative_position_bias_table": {"decay_mult": 0.0},
                "norm": {"decay_mult": 0.0},
            }
        },
    }

    # Default Hooks
    default_hooks = {
        "timer": {"type": "IterTimerHook"},
        "logger": {"type": "LoggerHook", "interval": 10},
        "param_scheduler": {"type": "ParamSchedulerHook"},
        "checkpoint": {
            "type": "CheckpointHook",
            "interval": 1,
            "save_best": "coco/bbox_mAP",
            "rule": "greater",
            "max_keep_ckpts": 2,
        },
        "sampler_seed": {"type": "DistSamplerSeedHook"},
    }

    # Base configuration dictionary
    cfg_dict = {
        "model": model_cfg,
        "train_dataloader": train_dataloader,
        "val_dataloader": val_dataloader,
        "val_evaluator": val_evaluator,
        "optim_wrapper": optim_wrapper,
        "default_hooks": default_hooks,
        "work_dir": work_dir,
        "default_scope": "mmdet",
        "env_cfg": {
            "cudnn_benchmark": config.training.cudnn_benchmark,
            "mp_cfg": {"mp_start_method": "fork", "opencv_num_threads": 0},
            "dist_cfg": {"backend": "nccl"},
        },
        "log_level": "INFO",
        "load_from": None,
        "resume": False,
    }

    return Config(cfg_dict)
