from torch.utils.data import Dataset
import json
from .utils import load_image
from data.datasets.test import get_file_list, make_train_test


class BasicDataset(Dataset):
    def __init__(self, data_list=None, transform=None):
        self.data_list = data_list
        self.transform = transform

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, idx):
        data = {}   # 이거 제일 중요! 어떻게 만들지 -> line by line / folder etc..
        img_dir, text_dir = self.data_list[idx]
        img = load_image(img_dir, type='RGB')   # imread 함수 만들.. 거나 cv2 혹은 PIL로 하거나  +  'RGB'와 'L' 선택하는 함수 만들기
        current_shape = img.size   # 이게 필요할지 안할지.. 우선..

        if self.transform is not None:
            img = self.transform(img)

        data = {}
        with open(text_dir, "r") as json_file:
            json_data = json.load(json_file)
            for i in range(len(json_data['shapes'])):
                data['file_name'] = json_data['imagePath']
                data['label'] = json_data['shapes'][i]['label']
                data['text_polys'] = json_data['shapes'][i]['points']

        return img, data, current_shape


    # @staticmethod
    # def collate_fn(batch):
    #     img, label, path, shapes = zip(*batch)   # transposed
    #     for i, l in enumerate(label):
    #         l[:, 0] = i   # add target image index for build_targets()
    #     return torch.stack(img, 0), torch.cat(label, 0), path, shape
