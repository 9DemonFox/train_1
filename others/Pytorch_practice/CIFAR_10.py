import torch as t
import torchvision as tv
import torchvision.transforms as transform
from torchvision.transforms import ToPILImage
import numpy as np
from PIL import Image

show = ToPILImage()  # 把tensor转化为Image

transform = transform.Compose([
    transform.ToTensor(),
    transform.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

trainset = tv.datasets.CIFAR10(
    root="./",
    train=True,
    download=True,
    transform=transform
)

trainloader = t.utils.data.DataLoader(
    trainset,
    batch_size=4,
    shuffle=True,
    num_workers=2
)

testset = tv.datasets.CIFAR10(
    root='./',
    train=False,
    download=True,
    transform=transform)

testloader = t.utils.data.DataLoader(
    testset,
    batch_size=4,
    shuffle=False,
    num_workers=2)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

(data, label) = trainset[100]
data = (data + 1) / 2  # 还原被归一化的数据

print(data.shape)
data = data.reshape(3, 32, 32)

pic = ToPILImage()(data)

pic.show()

print(classes[label])

import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super
