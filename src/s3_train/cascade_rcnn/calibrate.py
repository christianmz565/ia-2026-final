"""Timing Calibration module.

Measures epoch execution speed on local GPU hardware (discarding 1st warmup iteration)
and dynamically calculates total epochs required to keep training time strictly between 3 and 5 hours.
"""

import logging
import time

import numpy as np
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

logger = logging.getLogger("CascadeRCNN.Calibrate")


def calibrate_training_epochs(
    model: torch.nn.Module,
    train_loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    scaler: torch.amp.grad_scaler.GradScaler,
    device: torch.device,
    amp_enabled: bool = True,
    calibration_batches: int = 15,
    target_min_hours: float = 3.0,
    target_max_hours: float = 5.0,
) -> tuple[int, float, float]:
    """Execute warmup and micro-benchmarking steps to estimate epoch duration and calculate total epochs.

    Returns:
        Tuple of (calculated_epochs, estimated_total_seconds, time_per_epoch_seconds)
    """
    logger.info("--- STARTING TIMING CALIBRATION ---")
    model.train()

    batches_processed = 0
    total_batch_time = 0.0

    target_min_seconds = target_min_hours * 3600.0
    target_max_seconds = target_max_hours * 3600.0
    target_mid_seconds = (target_min_seconds + target_max_seconds) / 2.0

    # 1. Warmup iteration (discarded from timing)
    logger.info("Executing CUDA warmup iteration (discarded from timing metrics)...")
    for images, targets in train_loader:
        images = [img.to(device) for img in images]
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        optimizer.zero_grad()
        with torch.amp.autocast_mode.autocast("cuda", enabled=amp_enabled and device.type == "cuda"):
            loss_dict = model(images, targets)
            losses = torch.stack(list(loss_dict.values())).sum()

        if scaler is not None and amp_enabled:
            scaler.scale(losses).backward()
            scaler.step(optimizer)
            scaler.update()
        else:
            losses.backward()
            optimizer.step()

        # Warmup finished
        break

    torch.cuda.synchronize() if device.type == "cuda" else None

    # 2. Benchmark calibration iterations
    logger.info(f"Benchmarking {calibration_batches} calibration iterations...")
    pbar = tqdm(total=calibration_batches, desc="Calibration", leave=False)

    for images, targets in train_loader:
        if batches_processed >= calibration_batches:
            break

        images = [img.to(device) for img in images]
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        t_start = time.perf_counter()

        optimizer.zero_grad()
        with torch.amp.autocast_mode.autocast("cuda", enabled=amp_enabled and device.type == "cuda"):
            loss_dict = model(images, targets)
            losses = torch.stack(list(loss_dict.values())).sum()

        if scaler is not None and amp_enabled:
            scaler.scale(losses).backward()
            scaler.step(optimizer)
            scaler.update()
        else:
            losses.backward()
            optimizer.step()

        torch.cuda.synchronize() if device.type == "cuda" else None
        t_end = time.perf_counter()

        step_time = t_end - t_start
        total_batch_time += step_time
        batches_processed += 1
        pbar.update(1)

    pbar.close()

    avg_batch_time = total_batch_time / max(1, batches_processed)
    total_batches_per_epoch = len(train_loader)
    estimated_epoch_time_sec = avg_batch_time * total_batches_per_epoch

    # Calculate required epochs to target midpoint (~4 hours)
    target_epochs = int(round(target_mid_seconds / estimated_epoch_time_sec))

    # Ensure training time stays strictly within [3 hours, 5 hours]
    est_total_seconds = target_epochs * estimated_epoch_time_sec

    if est_total_seconds < target_min_seconds:
        target_epochs = int(np.ceil(target_min_seconds / estimated_epoch_time_sec))
        est_total_seconds = target_epochs * estimated_epoch_time_sec

    if est_total_seconds > target_max_seconds:
        target_epochs = int(np.floor(target_max_seconds / estimated_epoch_time_sec))
        target_epochs = max(1, target_epochs)
        est_total_seconds = target_epochs * estimated_epoch_time_sec

    logger.info("--- TIMING CALIBRATION RESULTS ---")
    logger.info(f"Average batch time: {avg_batch_time:.4f} seconds")
    logger.info(
        f"Batches per epoch: {total_batches_per_epoch} | Estimated single epoch duration: {estimated_epoch_time_sec / 60.0:.2f} minutes ({estimated_epoch_time_sec:.2f} seconds)"
    )
    logger.info(
        f"Calculated Total Epochs: {target_epochs} | Estimated Total Duration: {est_total_seconds / 3600.0:.2f} hours ({est_total_seconds / 60.0:.2f} minutes)"
    )

    return target_epochs, est_total_seconds, estimated_epoch_time_sec
