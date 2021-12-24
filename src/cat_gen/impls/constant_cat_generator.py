import cv2

from src.cat_gen.cat_generator import CatGenerator


class ConstantCatGenerator(CatGenerator):

    CONSTANT_CAT_LOCATION = "data/octocat.png"

    def __init__(self):
        super(ConstantCatGenerator, self).__init__()
        self.cat = cv2.imread(self.CONSTANT_CAT_LOCATION)

    def generate_cat(self):
        return self.cat
