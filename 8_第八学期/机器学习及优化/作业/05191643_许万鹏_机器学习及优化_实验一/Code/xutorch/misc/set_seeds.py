import os
import torch
import random
import numpy as np


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
