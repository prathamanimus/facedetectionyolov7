import torch
print("GPU available: ", torch.cuda.is_available())
torch.cuda.device_count()
torch.cuda.current_device()
torch.cuda_get_device_name(0)