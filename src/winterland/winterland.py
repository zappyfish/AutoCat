import cv2


class Winterland:

    def __init__(self, winterland_file_path):
        self.img = cv2.imread(winterland_file_path)

    def add_cat(self, cat):
        pass

    def write_winterland_to_file(self, file_path):
        cv2.imwrite(file_path, self.img)

    def display_winterland(self):
        cv2.imshow("Winterland", self.img)
        cv2.waitKey(0)
