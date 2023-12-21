import torch
from torch.optim import Optimizer


class SimpleSGD(Optimizer):
    def __init__(self, params, lr=0.01, momentum=0):
        defaults = dict(lr=lr, momentum=momentum)
        super(SimpleSGD, self).__init__(params, defaults)

    def step(self):
        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue
                grad = p.grad.data
                state = self.state[p]

                lr = group['lr']
                momentum = group['momentum']
                if 'momentum_buffer' not in state:
                    buf = state['momentum_buffer'] = torch.zeros_like(p.data)
                else:
                    buf = state['momentum_buffer']
                # buf = momentum * buf + grad
                buf.mul_(momentum).add_(grad)

                # p.data += -self.lr * buf
                p.data.add_(buf, alpha=-lr)       # new
