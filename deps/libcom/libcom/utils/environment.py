import torch


def check_gpu_device(device):
    if not torch.cuda.is_available():
        return torch.device('cpu')
    if isinstance(device, (int, str)):
        device = int(device)
        assert 0 <= device < torch.cuda.device_count(), f'invalid device id: {device}'
        device = torch.device(f'cuda:{device}')
    if isinstance(device, torch.device):
        return device
    raise Exception(f'invalid device type: type({type(device)})={device}')
