import logging
import sys

from geometry_utils import generate_list_of_points
from image_utils import ImageHandler


def main(img_filepath):
    logging.basicConfig(level=logging.INFO)
    logging.debug("Running main")

    # Get image data
    img_h = ImageHandler(img_filepath)

    # Identify centre and radius of circle
    centre = img_h.centre
    radius = int(img_h.width / 2)

    # Uncomment to debug
    # from geometry_utils import get_point_at_distance
    # for theta in range(0, 360):
    #     point = get_point_at_distance(theta, radius, centre)
    #     img_h.img[point.x - 1, point.y - 1] = 0
    #
    #     print(theta, point)
    #     img_h.show_img(10)

    # Increment value of theta
    for theta in range(0, 360, 1):
        # For each value of theta identify the the points
        list_of_points = generate_list_of_points(theta, radius, centre)

        # Uncomment to debug
        # for point in list_of_points:
        #     img_h.img[point.x - 1, point.y - 1] = 0
        # if theta % 45 == 0:
        #     img_h.show_img(1000)

        # Add the intensity of the pixels
        integral = img_h.add_intensity_of_points(list_of_points)

        # store value of theta and value of pixel
        print("%.2f, %d" % (theta, integral))

    # Uncomment to debug
    # img_h.show_img(0)


if __name__ == "__main__":
    filepath = "./img.png"
    if len(sys.argv) == 2:
        filepath = sys.argv[1]

    main(filepath)
