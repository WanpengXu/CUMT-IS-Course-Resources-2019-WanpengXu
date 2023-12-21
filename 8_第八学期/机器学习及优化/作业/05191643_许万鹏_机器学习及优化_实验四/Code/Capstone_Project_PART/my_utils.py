import os
import numpy as np
import time
import random
import torch
from torch.autograd import Variable


def set_seeds(seed):
    torch.manual_seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    # if torch.backends.cudnn.is_available():
    #     torch.backends.cudnn.benchmark = False
    #     torch.backends.cudnn.deterministic = True


def get_device():
    return torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


def get_run_time(f, *args):
    """
    Call a function f with args and return the time (in seconds) that it took to execute.
    """
    tic = time.time()
    result = f(*args)
    toc = time.time()
    return toc - tic, result


def _normalize(t, mean, std):
    t[:, 0, :, :] = (t[:, 0, :, :] - mean[0]) / std[0]
    t[:, 1, :, :] = (t[:, 1, :, :] - mean[1]) / std[1]
    t[:, 2, :, :] = (t[:, 2, :, :] - mean[2]) / std[2]

    return t


def CWLoss(logits, target, kappa=-0., tar=False, num_classes=10):
    target = torch.ones(logits.size(0)).type(torch.cuda.FloatTensor).mul(target.float())
    target_one_hot = Variable(torch.eye(num_classes).type(torch.cuda.FloatTensor)[target.long()].cuda())

    real = torch.sum(target_one_hot * logits, 1)
    other = torch.max((1 - target_one_hot) * logits - (target_one_hot * 10000), 1)[0]
    kappa = torch.zeros_like(other).fill_(kappa)

    if tar:
        return torch.sum(torch.max(other - real, kappa))
    else:
        return torch.sum(torch.max(real - other, kappa))
