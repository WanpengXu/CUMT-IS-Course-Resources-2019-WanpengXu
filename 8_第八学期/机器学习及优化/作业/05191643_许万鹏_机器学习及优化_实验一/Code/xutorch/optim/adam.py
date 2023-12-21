import torch
import torch.optim as optim


# extend from torch.optim.Optimizer, 'zero_grad' method can be omitted
class SimpleAdam(optim.Optimizer):
    def __init__(self, params, lr=0.001, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
        defaults = dict(lr=lr, betas=betas, eps=eps, weight_decay=weight_decay)
        super(SimpleAdam, self).__init__(params, defaults)

        for group in self.param_groups:
            for param in group['params']:
                state = self.state[param]
                state['step'] = 0
                state['exp_avg'] = torch.zeros_like(param.data)
                state['exp_avg_sq'] = torch.zeros_like(param.data)

    def step(self):
        for group in self.param_groups:
            for param in group['params']:  # 这个params其实是weights而不是模型的超参数
                if param.grad is None:
                    continue
                grad = param.grad.data

                state = self.state[param]
                state['step'] += 1

                beta1, beta2 = group['betas']
                exp_avg = state['exp_avg']
                exp_avg_sq = state['exp_avg_sq']

                exp_avg.mul_(beta1).add_(grad, alpha=1 - beta1)
                exp_avg_sq.mul_(beta2).addcmul_(grad, grad, value=1 - beta2)

                bias_correction1 = 1 - beta1 ** state['step']
                bias_correction2 = 1 - beta2 ** state['step']

                step_size = group['lr'] * (bias_correction2 ** 0.5) / bias_correction1

                if group['weight_decay'] != 0:
                    param.data.add_(-group['lr'] * group['weight_decay'], param.data)

                param.data.add_(exp_avg / (exp_avg_sq.sqrt() + group['eps']), alpha=-step_size)

# from-scratch
# class SimpleAdam:
#     def __init__(self, params, lr=0.001, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
#         self.params = list(params)
#         self.lr = lr
#         self.betas = betas
#         self.eps = eps
#         self.weight_decay = weight_decay
#         self.state = []

#         for param in self.params:
#             state = {
#                 'step': 0,
#                 'exp_avg': torch.zeros_like(param.data),
#                 'exp_avg_sq': torch.zeros_like(param.data)
#             }
#             self.state.append(state)

#     def zero_grad(self):
#         for param in self.params:
#             if param.grad is not None:
#                 param.grad.detach_()
#                 param.grad.zero_()

#     def step(self):
#         for i, param in enumerate(self.params):
#             if param.grad is None:
#                 continue
#             grad = param.grad.data
#             state = self.state[i]

#             state['step'] += 1

#             beta1, beta2 = self.betas
#             exp_avg = state['exp_avg']
#             exp_avg_sq = state['exp_avg_sq']

#             exp_avg.mul_(beta1).add_(grad, alpha=1 - beta1)
#             exp_avg_sq.mul_(beta2).addcmul_(grad, grad, value=1 - beta2)

#             bias_correction1 = 1 - beta1 ** state['step']
#             bias_correction2 = 1 - beta2 ** state['step']

#             step_size = self.lr * (bias_correction2 ** 0.5) / bias_correction1

#             if self.weight_decay != 0:
#                 param.data.add_(-self.lr * self.weight_decay, param.data)

#             param.data.add_(exp_avg / (exp_avg_sq.sqrt() + self.eps), alpha=-step_size)
