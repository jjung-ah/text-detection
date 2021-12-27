from dataclasses import dataclass

import torch

from datasets.types import Tensor

@dataclass
class DataInfo:
    image_path_lists: list
    image_nums: int

@dataclass
class ValInfo:
    loss: dict
    model_path: str
    model: Tensor

@dataclass
class DataInfoSemantic:
    label_dicts: dict
    names: list

@dataclass
class MetaInfoSemantic:
    image_path: str
    mask_path: str

@dataclass
class MetricResults:
    precisions: list
    recalls: list
    f_scores: list