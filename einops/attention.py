import torch
import torch.nn as nn
import torch.nn.functional as F
from einops.layers.torch import Rearrange

class AttnBlock3d(nn.Module):
  """Channel-wise 3D self-attention block."""
  def __init__(self, channels):
    super().__init__()
    torch.random.manual_seed(42)
    self.norm = nn.GroupNorm(num_groups=1, num_channels=channels, eps=1e-6)
    self.qkv = nn.Conv3d(channels, channels*3, kernel_size=1)
    self.spatial_flatten = Rearrange(pattern="b c h w d -> b c (h w d)")
    self.proj = nn.Conv3d(channels, channels, kernel_size=1)
    self.scale = int(channels) ** (-0.5)

  def forward(self, x):
    B, C, H, W, D = x.shape
    q,k,v = self.qkv(self.norm(x)).chunk(3, dim=1)

    q = self.spatial_flatten(q)
    k = self.spatial_flatten(k)
    v = self.spatial_flatten(v)

    w = torch.einsum('b c q, b c k -> b q k', q, k) * self.scale
    w = F.softmax(w, dim=-1)
    h = torch.einsum("b q k , b c k -> b c q", w,v)
    h = torch.reshape(h, (B, C, H, W, D))
    h = self.proj(h)

    return x + h