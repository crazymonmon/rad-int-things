import cv2

from point import Point


class ImageHandler:

    def __init__(self, filepath):
        self.img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        self.rows, self.cols = self.img.shape

    def get_img_centre(self):
        return Point(int(self.rows/2), int(self.cols/2))

    def get_img_width(self):
        return self.rows if self.rows <= self.cols else self.cols

    def add_intensity_of_points(self, list_of_points: list[Point]):
        intensity_sum = 0

        for point in list_of_points:
            intensity_sum = intensity_sum + self.img[point.x, point.y]

        return intensity_sum
