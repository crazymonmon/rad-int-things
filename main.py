import logging

from geometry_utils import generate_list_of_points
from image_utils import ImageHandler


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running main")

    # Get image data
    img_filepath = ""
    img_h = ImageHandler(img_filepath)

    # Identify centre and radius of circle
    centre = img_h.get_img_centre()
    radius = int(img_h.get_img_width()/2)

    # Increment value of theta
    for theta in range(0, 180+1):
        # for each value of theta identify the the points and sum the intensity
        list_of_point = generate_list_of_points(theta, radius, centre)
        integral = img_h.add_intensity_of_points(list_of_point)

        # store value of theta and value of pixel
        print("Theta: ", theta, " Integral: ", integral)


if __name__ == "__main__":
    main()
