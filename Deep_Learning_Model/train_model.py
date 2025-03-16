import torch
import torch.nn as nn
import torch.optim as optim

class WatermarkNet(nn.Module):
    def __init__(self):
        super(WatermarkNet, self).__init__()
        self.conv = nn.Conv2d(1, 16, 3, stride=1)
        self.fc = nn.Linear(16, 1)

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return torch.sigmoid(self.fc(x))

