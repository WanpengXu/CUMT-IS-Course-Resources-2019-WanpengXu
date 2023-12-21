import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

###########################
# Generator: Resnet
###########################

# To control feature map in generator
ngf = 64


class GeneratorResnet(nn.Module):
    def __init__(self, inception=False, data_dim='high', eps=1.0, evaluate=False):
        '''
        :param inception: if True crop layer will be added to go from 3x300x300 t0 3x299x299.
        :param data_dim: for high dimentional dataset (imagenet) 6 resblocks will be add otherwise only 2.
        '''
        super(GeneratorResnet, self).__init__()
        self.inception = inception
        self.data_dim = data_dim
        # Input_size = 3, n, n
        self.block1 = nn.Sequential(
            nn.ReflectionPad2d(3),
            nn.Conv2d(3, ngf, kernel_size=7, padding=0, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True)
        )

        # Input size = 3, n, n
        self.block2 = nn.Sequential(
            nn.Conv2d(ngf, ngf * 2, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True)
        )

        # Input size = 3, n/2, n/2
        self.block3 = nn.Sequential(
            nn.Conv2d(ngf * 2, ngf * 4, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True)
        )

        # Input size = 3, n/4, n/4
        # Residual Blocks: 6
        self.resblock1 = ResidualBlock(ngf * 4)
        self.resblock2 = ResidualBlock(ngf * 4)
        if self.data_dim == 'high':
            self.resblock3 = ResidualBlock(ngf * 4)
            self.resblock4 = ResidualBlock(ngf * 4)
            self.resblock5 = ResidualBlock(ngf * 4)
            self.resblock6 = ResidualBlock(ngf * 4)

        # Input size = 3, n/4, n/4
        self.upsampl_inf1 = nn.Sequential(
            nn.ConvTranspose2d(ngf * 4, ngf * 2, kernel_size=3, stride=2, padding=1, output_padding=1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True)
        )

        # Input size = 3, n/2, n/2
        self.upsampl_inf2 = nn.Sequential(
            nn.ConvTranspose2d(ngf * 2, ngf, kernel_size=3, stride=2, padding=1, output_padding=1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True)
        )

        # Input size = 3, n, n
        self.blockf_inf = nn.Sequential(
            nn.ReflectionPad2d(3),
            nn.Conv2d(ngf, 3, kernel_size=7, padding=0)
        )

        # Input size = 3, n/4, n/4
        self.upsampl_01 = nn.Sequential(
            nn.ConvTranspose2d(ngf * 4, ngf * 2, kernel_size=3, stride=2, padding=1, output_padding=1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True)
        )

        # Input size = 3, n/2, n/2
        self.upsampl_02 = nn.Sequential(
            nn.ConvTranspose2d(ngf * 2, ngf, kernel_size=3, stride=2, padding=1, output_padding=1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True)
        )

        # Input size = 3, n, n
        self.blockf_0 = nn.Sequential(
            nn.ReflectionPad2d(3),
            nn.Conv2d(ngf, 1, kernel_size=7, padding=0)
        )

        self.crop = nn.ConstantPad2d((0, -1, -1, 0), 0)

        self.eps = eps
        self.evaluate = evaluate

    def forward(self, input):
        x = self.block1(input)
        x = self.block2(x)
        x = self.block3(x)
        x = self.resblock1(x)
        x = self.resblock2(x)
        if self.data_dim == 'high':
            x = self.resblock3(x)
            x = self.resblock4(x)
            x = self.resblock5(x)
            x = self.resblock6(x)
        code = x
        x = self.upsampl_inf1(code)
        x = self.upsampl_inf2(x)
        x = self.blockf_inf(x)
        if self.inception:
            x = self.crop(x)
        x_inf = self.eps * torch.tanh(x)  # Output range [-eps, eps]
        x = self.upsampl_01(code)
        x = self.upsampl_02(x)
        x = self.blockf_0(x)
        if self.inception:
            x = self.crop(x)
        x = (torch.tanh(x) + 1) / 2
        if self.evaluate:
            x_0 = torch.where(x < 0.5, torch.zeros_like(x).detach(), torch.ones_like(x).detach())
        else:
            x_0 = torch.where(torch.rand(x.shape).cuda() < 0.5, x,
                              torch.where(x < 0.5, torch.zeros_like(x), torch.ones_like(x)).detach())
        # print('==> DEBUG START')
        # print(x_inf.size())
        # print(x_0.size())
        # print(input.size())
        # print('==> DEBUG END')
        x_out = torch.clamp(x_inf * x_0 + input, min=0, max=1)
        return x_out, x_inf, x_0, x


class ResidualBlock(nn.Module):
    def __init__(self, num_filters):
        super(ResidualBlock, self).__init__()
        self.block = nn.Sequential(
            nn.ReflectionPad2d(1),
            nn.Conv2d(in_channels=num_filters, out_channels=num_filters, kernel_size=3, stride=1, padding=0,
                      bias=False),
            nn.BatchNorm2d(num_filters),
            nn.ReLU(True),

            nn.Dropout(0.5),

            nn.ReflectionPad2d(1),
            nn.Conv2d(in_channels=num_filters, out_channels=num_filters, kernel_size=3, stride=1, padding=0,
                      bias=False),
            nn.BatchNorm2d(num_filters)
        )

    def forward(self, x):
        residual = self.block(x)
        return x + residual


if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # netG = GeneratorResnet(data_dim='high').to(device)
    netG = GeneratorResnet(eps=10 / 255., evaluate=True, data_dim='high').to(device)
    netG.load_state_dict(torch.load('/root/autodl-tmp/TSAA_Capstone_Project_Big_Files/pretrained_generators/netG_-1_res50_eps10_epoch9_loss96.1.pth'))
    netG.eval()
    # test_sample = torch.rand(10, 3, 32, 32).to(device)
    # print('Generator output:', netG(test_sample)[0].size())
    # print('Generator parameters:', sum(p.numel() for p in netG.parameters() if p.requires_grad))

    import torchvision.datasets as datasets
    from torch.utils.data import DataLoader
    import torchvision.transforms as transforms

    data_transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    test_dir = '/root/autodl-tmp/TSAA_Capstone_Project_Big_Files/dataset/CIFAR_10/cifar-10-batches-py/test'
    test_set = datasets.ImageFolder(test_dir, data_transform)
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=10, shuffle=True, num_workers=12, pin_memory=True)

    for i, (img, label) in enumerate(test_loader):
        img, label = img.to(device), label.to(device)
        adv, _, adv_0, adv_00 = netG(img)
        quit()
