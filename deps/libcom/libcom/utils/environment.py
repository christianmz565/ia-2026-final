import torch


def check_gpu_device(device):
    if not torch.cuda.is_available():
        return torch.device("cpu")
    if isinstance(device, torch.device):
        return device
    if isinstance(device, str):
        if device == "cpu":
            return torch.device("cpu")
        if device.startswith("cuda:"):
            return torch.device(device)
        if device == "cuda":
            return torch.device("cuda:0")
        if device.isdigit():
            device = int(device)
        else:
            return torch.device(device)
    if isinstance(device, int):
        assert 0 <= device < torch.cuda.device_count(), f"invalid device id: {device}"
        return torch.device(f"cuda:{device}")
    raise Exception(f"invalid device type: type({type(device)})={device}")

