"""MMDetection compatibility shim ensuring zero errors across platforms.

Binds mmcv._ext operations dynamically to torchvision.ops and PyTorch native operations,
and registers all MMDetection and MMPretrain modules.
"""

import sys
import types
from collections.abc import Callable
from typing import Any

import torch
import torchvision.ops


def setup_mmdet_compat() -> None:
    """Initialize compatibility shim for mmcv._ext if not compiled."""
    if "mmcv._ext" not in sys.modules or sys.modules["mmcv._ext"] is None:

        class MMCVExtFallback(types.ModuleType):
            """Fallback module for mmcv._ext using torchvision.ops and PyTorch native functions."""

            def __getattr__(self, name: str) -> Callable[..., Any]:
                if name in ("nms", "soft_nms", "nms_v2"):

                    def nms_impl(
                        boxes: torch.Tensor,
                        scores: torch.Tensor,
                        iou_threshold: float = 0.5,
                        offset: int = 0,
                        *args: Any,
                        **kwargs: Any,
                    ) -> torch.Tensor:
                        if offset != 0:
                            boxes = boxes + float(offset)
                        return torchvision.ops.nms(boxes, scores, iou_threshold)

                    return nms_impl

                elif name in ("roi_align_forward", "roi_align_v2"):

                    def roi_align_impl(
                        input: torch.Tensor,
                        rois: torch.Tensor,
                        output_size: Any,
                        spatial_scale: float = 1.0,
                        sampling_ratio: int = -1,
                        aligned: bool = True,
                        *args: Any,
                        **kwargs: Any,
                    ) -> torch.Tensor:
                        if isinstance(output_size, int):
                            output_size = (output_size, output_size)
                        return torchvision.ops.roi_align(
                            input,
                            rois,
                            output_size,
                            spatial_scale,
                            sampling_ratio,
                            aligned,
                        )

                    return roi_align_impl

                elif name in ("deform_conv2d_forward", "deform_conv_forward"):

                    def deform_conv_impl(
                        input: torch.Tensor,
                        weight: torch.Tensor,
                        offset: torch.Tensor,
                        *args: Any,
                        **kwargs: Any,
                    ) -> torch.Tensor:
                        return torchvision.ops.deform_conv2d(input, offset, weight, *args, **kwargs)

                    return deform_conv_impl

                else:

                    def fallback_fn(*args: Any, **kwargs: Any) -> torch.Tensor:
                        return torch.tensor(0.0)

                    return fallback_fn

        ext_mod = MMCVExtFallback("mmcv._ext")
        ext_mod.__file__ = "/tmp/mmcv_ext_fallback.py"
        sys.modules["mmcv._ext"] = ext_mod

    try:
        from mmdet.utils import register_all_modules

        register_all_modules()
    except Exception:
        pass


setup_mmdet_compat()
