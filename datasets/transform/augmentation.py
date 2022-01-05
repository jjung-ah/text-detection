import os
import shutil
import cv2
import random

class Augmentation:
    def __init__(self, train_set, test_set, data_dir):
        self.save_dir = self._get_augmentation_dir(data_dir)
        self.train_list = train_set
        self.test_list = test_set
        self.data_count = len(train_set) + len(test_set)

    def _get_augmentation_dir(self, data_dir):
        root, dirs, files = os.walk(data_dir)
        root_path = 
