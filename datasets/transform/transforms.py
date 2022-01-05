# 이 부분은 build.py로 따로 만들기

# from torchvision import transforms


# def _train_transforms():
#     return transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Resize((,)),
#         transforms.RandomVerticalFlip(p=0.5)
#     ])


# def _val_transforms():
#     return transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Resize((,))
#     ])

from torch import Tensor
from torchvision.transforms.functional import _interpolation_modes_from_int

import torch
import torchvision
import torchvision.transforms as T
import torchvision.transforms.functional as F
import random


class Compose(object):
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, image):
        for trans in self.transforms:
            image = trans(image)
        return image


class ToTensor(object):
    def __init__(self, image):
        self.image = image

    def __call__(self, image):
        return F.to_tensor(image)


class Resize(object):
    def __init__(self, size, interpolation):
        self.size = size
        self.interpolation = _interpolation_modes_from_int(interpolation)

    def __call__(self, image):
        return F.resize(image, (self.size, self.size), self.interpolation)


class ToPILImage(object):
    def __init__(self, mode=None):
        self.mode = mode

    def __call__(self, image):
        return F.to_pil_image(image, self.mode)


class RandomVerticalFlip(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def __call__(self, image):
        if torch.rand(1) < self.ratio:
            image = F.vflip(image)
        return image


class Normalize(object):
    def __init__(self, mean, std, inplace=False):
        self.mean = mean
        self.std = std
        self.inplace = inplace

    def __call__(self, tensor: Tensor) -> Tensor:
        return F.normalize(tensor, self.mean, self.std, self.inplace)
