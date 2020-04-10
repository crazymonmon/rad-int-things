import logging

import cv2

from geometry_utils import generate_list_of_points
from image_utils import ImageHandler


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running main")

    # Get image data
    img_filepath = "./img.png"
    img_h = ImageHandler(img_filepath)

    # Identify centre and radius of circle
    centre = img_h.centre
    radius = int(img_h.width / 2)

    # Increment value of theta
    for theta in range(0, 180+1):
        # for each value of theta identify the the points and sum the intensity
        list_of_points = generate_list_of_points(theta, radius, centre)

        for point in list_of_points:
            img_h.img[point.x - 1, point.y - 1] = 0

        if theta == 45 or theta == 90 or theta == 135:
            cv2.imshow("test", img_h.img)
            cv2.waitKey(0)

        integral = img_h.add_intensity_of_points(list_of_points)

        # store value of theta and value of pixel
        # print("%.2f, %d" % (theta, integral))
    cv2.imshow("test", img_h.img)
    cv2.waitKey(0)




if __name__ == "__main__":
    main()
