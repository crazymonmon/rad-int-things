import logging

import cv2

from point import Point


class ImageHandler:

    def __init__(self, filepath):
        self.img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

        if self.img is None:
            raise Exception("Invalid image.")

        rows, cols = self.img.shape
        self._centre = Point(int(rows / 2), int(cols / 2))
        self._width = rows if rows <= cols else cols

        logging.debug("Loaded image of size %d x %d" % (cols, rows))
        logging.debug("Width: %s" % self.width)
        logging.debug("Centre: %s" % self.centre)

    @property
    def centre(self):
        return self._centre

    @property
    def width(self):
        return self._width

    def get_intensity(self, point: Point):
        return self.img[int(point.x - 1), int(point.y - 1)]

    def add_intensity_of_points(self, list_of_points: list):
        intensity_sum = 0

        for point in list_of_points:
            # FIXME: Why does the x and y need to be cast to int?
            intensity_sum = intensity_sum + self.img[int(point.x - 1), int(point.y - 1)]
            # logging.debug("Intensity is %d at %s" % (self.img[int(point.x - 1), int(point.y - 1)], point))

        return intensity_sum

    def show_img(self, delay=0):
        cv2.imshow("img", self.img)
        cv2.waitKey(delay)
