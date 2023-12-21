from torch.backends import cudnn

from my_utils import set_seeds, _normalize, get_device, CWLoss
import os
import time
import argparse
from shutil import copyfile
import logging

import torchvision
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torchvision.utils as vutils

from generators import GeneratorResnet

from pytorch_cifar.models import *


def get_args():
    parser = argparse.ArgumentParser(description='Training code for generating sparse adversarial examples')
    parser.add_argument('--train_dir',
                        default='/root/autodl-tmp/TSAA_Capstone_Project_Big_Files/dataset/CIFAR_10/cifar-10-batches-py/train',
                        help='Path of train set')
    parser.add_argument('--num_classes', type=int, default=10, help='Number of dataset classes')
    parser.add_argument('--model', type=str,
                        default='mobile',
                        help='Model against GAN is trained: incv3, res50')
    parser.add_argument('--model_weight', type=str,
                        default='/root/autodl-tmp/TSAA_Capstone_Project/code/pytorch_cifar/checkpoint/mobile/20230409_ckpt.pth',
                        help='Weight of model')
    parser.add_argument('--eps', type=int,
                        default=255, help='Perturbation Budget')  # CIFAR-10不能调太低（?），一共也没多少像素
    parser.add_argument('--target', type=int,
                        default=-1, help='-1 if untargeted')
    parser.add_argument('--batch_size', type=int,
                        default=32, help='Number of trainig samples/batch')
    parser.add_argument('--epochs', type=int,
                        default=10, help='Number of training epochs')
    # parser.add_argument('--lr', type=float, default=0.00001, help='Initial learning rate for adam')   # res50
    # parser.add_argument('--lam_spa', type=float,
    #                     default=0.0001, help='lambda of spatial loss')
    # parser.add_argument('--lam_qua', type=float,
    #                     default=0.0001, help='lambda of quadratic loss')
    parser.add_argument('--lr', type=float,
                        default=0.0001, help='Initial learning rate for adam')  # 是不是这里有问题啊？根本就没收敛！
    parser.add_argument('--lam_spa', type=float,
                        default=0.005, help='lambda of spatial loss')
    parser.add_argument('--lam_qua', type=float,
                        default=0.0001, help='lambda of quadratic loss')
    return parser.parse_args()


now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
os.mkdir(os.path.join(now))

copyfile('my_train.py', os.path.join(now, 'my_train.py'))
copyfile('generators.py', os.path.join(now, 'generators.py'))

logging.basicConfig(level=logging.DEBUG, format='',
                    handlers=[logging.StreamHandler(), logging.FileHandler(os.path.join(now, 'output.log'))])

set_seeds(42)
device = get_device()
args = get_args()
# print(args)
logging.info(args)

# Model
model = None
if args.model == 'incv3':
    model = torchvision.models.inception_v3(init_weights=False, num_classes=args.num_classes)
elif args.model == 'res18':
    model = ResNet18()
elif args.model == 'res50':
    model = ResNet50()
elif args.model == 'res34':
    model = ResNet34()
elif args.model == 'res101':
    model = ResNet101()
elif args.model == 'res152':
    model = ResNet152()
elif args.model == 'vgg11':
    model = VGG('VGG11')
elif args.model == 'vgg13':
    model = VGG('VGG13')
elif args.model == 'vgg16':
    model = VGG('VGG16')
elif args.model == 'vgg19':
    model = VGG('VGG19')
elif args.model == 'google':
    model = GoogLeNet()
elif args.model == 'mobile':
    model = MobileNet()
elif args.model == 'mobilev2':
    model = MobileNetV2()
model = model.to(device)
if device != 'cpu':
    model = torch.nn.DataParallel(model)
    cudnn.benchmark = True
checkpoint = torch.load(args.model_weight)
model.load_state_dict(checkpoint['net_state_dict'])
model.eval()

# print(checkpoint['acc'])
logging.info(f"model_acc={checkpoint['acc']}")

# Input dimensions
# ImageNet中的图片大小不固定

# scale_size = 32
# img_size = 32
#
# # ResNet-50 接受 224*224
# if args.model in ['res50']:
#     scale_size = 256
#     img_size = 224
# # Inception 接受 299*299
# else:
#     scale_size = 300
#     img_size = 299

# Generator
if args.model == 'incv3':
    netG = GeneratorResnet(inception=True, eps=args.eps / 255., data_dim='high')
else:
    netG = GeneratorResnet(eps=args.eps / 255., data_dim='high')
netG = netG.to(device)

# Optimizer
optimG = optim.Adam(netG.parameters(), lr=args.lr, betas=(0.5, 0.999))
# optimG = optim.Adam(netG.parameters(), lr=args.lr, betas=(0.1, 0.999))
# optimG = optim.Adam(netG.parameters(), lr=args.lr)
# optimG = optim.SGD(netG.parameters(), lr=args.lr)

# Data
data_transform = transforms.Compose([
    # transforms.Resize(scale_size),
    # transforms.CenterCrop(img_size),
    # transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])


def normalize(t):
    # CIFAR-10 train dataset
    mean = (0.4914, 0.4822, 0.4465)
    std = (0.2023, 0.1994, 0.2010)
    return _normalize(t, mean, std)


train_set = datasets.ImageFolder(args.train_dir, data_transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=args.batch_size, shuffle=True, num_workers=12,
                                           pin_memory=True)
train_size = len(train_set)
# print('Training data size:', train_size)
logging.info(f'Training data size: {train_size}')

# Loss
criterion = CWLoss

# Training
# print('Label: {} \t Model: {} \t Dataset: {} \t Saving instances: {}'.format(
#     args.target, args.model, args.train_dir, args.epochs))
logging.info('Label: {} \t Model: {} \t Dataset: {} \t Saving instances: {}'.format(
    args.target, args.model, args.train_dir, args.epochs))

lam_spa = args.lam_spa
lam_qua = args.lam_qua

# 这两个值之间的相对关系很重要，但是绝对值应该也要改，不然就不考虑其他因素了
# res50
# lam_spa = 0.005  # lambda of spatial loss
# lam_qua = 0.0005  # lambda of quadratic loss

# vgg16
# lam_spa = 0.05  # lambda of spatial loss
# lam_qua = 0.005  # lambda of quadratic loss

# print(f'lambda_sparsity: {lam_spa}, lambda_quadratic: {lam_qua}')
logging.info(f'lambda_sparsity: {lam_spa}, lambda_quadratic: {lam_qua}')

# lam_spa = 0.009  # lambda of spatial loss
# lam_qua = 0.0005  # lambda of quadratic loss
for epoch in range(args.epochs):
    train_loss = 0
    for i, (img, gt) in enumerate(train_loader):
        img, gt = img.to(device), gt.to(device)

        if args.target == -1:
            label = model(normalize(img.clone().detach())).argmax(dim=-1).detach()
        else:
            label = torch.LongTensor(img.size(0))
            label.fill_(args.target)
            label = label.to(device)

        netG.train()
        optimG.zero_grad()

        adv, adv_inf, adv_0, adv_00 = netG(img)
        adv_img = adv.clone()

        adv_out = model(normalize(adv))
        if args.target == -1:
            # Gradient accent (Untargetted Attack)
            loss_adv = criterion(adv_out, label)
        else:
            # Gradient decent (Targetted Attack)
            loss_adv = criterion(adv_out, label, tar=True)
        loss_spa = torch.norm(adv_0, 1)
        bi_adv_00 = torch.where(adv_00 < 0.5, torch.zeros_like(adv_00), torch.ones_like(adv_00))
        loss_qua = torch.sum((bi_adv_00 - adv_00) ** 2)
        loss = loss_adv + lam_spa * loss_spa + lam_qua * loss_qua

        loss.backward()
        optimG.step()

        train_loss += loss

        if i % 100 == 0:
            adv_0_img = torch.where(adv_0 < 0.5, torch.zeros_like(adv_0), torch.ones_like(adv_0)).clone().detach()
            vutils.save_image(vutils.make_grid(adv_img, normalize=True, scale_each=True), now + '/adv.png')
            vutils.save_image(vutils.make_grid(img, normalize=True, scale_each=True), now + '/org.png')
            vutils.save_image(vutils.make_grid(adv_img - img, normalize=True, scale_each=True), now + '/noise.png')
            vutils.save_image(vutils.make_grid(adv_0_img * adv_inf, normalize=True, scale_each=True),
                              now + '/perturb.png')
            vutils.save_image(vutils.make_grid(adv_0_img, normalize=True, scale_each=True), now + '/mask.png')
            # print('l0:', torch.norm(adv_0_img, 0) / args.batch_size)
            logging.info(f'l0: {torch.norm(adv_0_img, 0) / args.batch_size}')
    torch.save(netG.state_dict(), os.path.join(now, 'netG_{}_{}_eps{}_epoch{}_lam_spa{}_loss{:.3}.pth'.format(
        args.target, args.model, args.eps, epoch, lam_spa, train_loss / len(train_loader))))

# os.system("/usr/bin/shutdown")
