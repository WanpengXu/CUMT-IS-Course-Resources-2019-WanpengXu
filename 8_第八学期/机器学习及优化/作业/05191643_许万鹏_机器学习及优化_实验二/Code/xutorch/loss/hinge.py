import torch
import torch.nn as nn


class Hinge(nn.Module):
    def __init__(self, c=0.01):
        super(Hinge, self).__init__()
        self.c = c

    def forward(self, outputs, labels, weight):
        # loss = torch.mean(torch.clamp(1 - labels * outputs, min=0)) + 0.01 * (weight.t() @ weight) / 2.0
        loss_part1 = torch.mean(torch.clamp(1 - labels * outputs, min=0))
        loss_part2 = self.c * torch.norm(weight, p=2) ** 2 / 2.0
        loss = loss_part1 + loss_part2

        return loss
