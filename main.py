import argparse
import logging

from geometry_utils import generate_list_of_points
from image_utils import ImageHandler


def main(args):
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level)

    # Get image data
    img_h = ImageHandler(args.img_filepath)

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
    theta = 0.0
    theta_step_size = args.step_size

    while theta < 360:
        # For each value of theta identify the the points
        list_of_points = generate_list_of_points(theta, radius, centre)

        # Uncomment to debug
        # for point in list_of_points:
        #     img_h.img[point.x - 1, point.y - 1] = 0
        # if theta % 45 == 0:
        #     img_h.show_img(1000)

        # Add the intensity of the pixels
        sum_of_intensity = img_h.add_intensity_of_points(list_of_points)

        # store value of theta and value of pixel
        if args.num_points:
            print("%.2f, %d" % (theta, len(list_of_points)))
        elif args.show_all_points:
            print("%.2f, %s" % (theta, ", ".join(list(map(lambda x: str(img_h.get_intensity(x)), list_of_points)))))
        else:
            print("%.2f, %d" % (theta, sum_of_intensity))

        # Increment theta
        theta = round(theta + theta_step_size, 2)

    # Uncomment to debug
    # img_h.show_img(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("img_filepath", help="Filepath of image")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--num_points", action="store_true", default=False,
                       help="Display number of points for every theta")
    group.add_argument("--show_all_points", action="store_true", default=False,
                       help="Display value of all the points for every theta")
    parser.add_argument("--step_size", metavar="N", default=1.0, type=float,
                        help="Degrees in which theta will be incremented. NOTE: Must be <= 1.")
    parser.add_argument("--verbose", action="store_true", default=False,
                        help="Verbose mode")

    parsed_args = parser.parse_args()

    main(parsed_args)
