import copy
import logging
import math

from point import Point


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running main")

    # Get image data
    # Identify centre and max width of image
    centre = Image.getImageCentre()
    width = Image.getWidth()
    # normalize image data
    Image.normalize()
    data = Image.getData()

    # Increment value of theta
    for theta in range(0,180+1):
        # for each value of theta identify the the points and sum the intensity
        list_of_point = generate_list_of_points(theta, width, centre)
        integral = sum(image, list_of_point)

        # store value of theta and value of pixel


def generate_list_of_points(theta: int, radius: int, centre: Point):
    if theta > 180:
        raise Exception("Theta greater than 180.")

    target_point = get_point_at_distance(theta, radius, centre)

    list_of_point = []
    # manhattan distance
    dx = target_point.x - centre.x
    dy = target_point.y - centre.y

    if theta <= 45:
        for x in range(centre.x, target_point.x + 1):
            y = centre.y + dy * (x - centre.x) / dx
            list_of_point.append(Point(x, y))
    elif theta > 135:
        for x in range(target_point.x, centre.x + 1):
            y = centre.y + dy * (x - centre.x) / dx
            list_of_point.append(Point(x, y))
    else:
        for y in range(centre.y, target_point.y + 1):
            x = centre.x + dx * (y - centre.y) / dy
            list_of_point.append(Point(x, y))

    return list_of_point


def get_point_at_distance(theta: int, radius: int, origin=Point(0,0)):
    # Create point from the origin
    point = Point()

    if theta == 0:
        point.x = origin.x + radius
    elif theta == 90:
        point.y = origin.y + radius
    elif theta == 180:
        point.x = origin.x + (-1 * radius)
    elif theta > 180:
        raise Exception("Value of theta > 180.")
    else:
        m = math.tan(math.radians(theta))
        dx = radius/(math.sqrt(1+(m*m)))
        dy = m * dx

        point.x = (origin.x + dx) if theta < 90 else (origin.x - dx)
        point.y = origin.y + dy

    return point








if __name__ == "__main__":
    main()
