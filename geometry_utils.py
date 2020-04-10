import logging
import math

from point import Point


def generate_list_of_points(theta: float, radius: int, centre: Point):
    list_of_points = []

    target_point = get_point_at_distance(theta, radius, centre)

    dx = target_point.x - centre.x
    dy = target_point.y - centre.y

    # TODO: Simplify this if condition
    if theta < 45:
        for x in range(centre.x, target_point.x + 1):
            # y  = y1 + (x - x1)/m
            y = centre.y + dy * (x - centre.x)/dx
            list_of_points.append(Point(x, y))
    elif theta < 90:
        for y in range(centre.y, target_point.y + 1):
            # x  = x1 + m * (y - y1)
            x = centre.x + dx * (y - centre.y)/dy
            list_of_points.append(Point(x, y))
    elif theta < 135:
        for y in range(centre.y, target_point.y + 1):
            # x  = x1 + m * (y - y1)
            x = centre.x + dx * (y - centre.y) / dy
            list_of_points.append(Point(x, y))
    elif theta < 180:
        for x in range(target_point.x, centre.x + 1):
            # y  = y1 + (x - x1)/m
            y = centre.y + dy * (x - centre.x)/dx
            list_of_points.append(Point(x, y))
    elif theta < 225:
        for x in range(target_point.x, centre.x + 1):
            # y  = y1 + (x - x1)/m
            y = centre.y + dy * (x - centre.x)/dx
            list_of_points.append(Point(x, y))
    elif theta < 270:
        for y in range(target_point.y, centre.y + 1):
            # x  = x1 + m * (y - y1)
            x = centre.x + dx * (y - centre.y)/dy
            list_of_points.append(Point(x, y))
    elif theta < 315:
        for y in range(target_point.y, centre.y + 1):
            # x  = x1 + m * (y - y1)
            x = centre.x + dx * (y - centre.y) / dy
            list_of_points.append(Point(x, y))
    elif theta < 360:
        for x in range(target_point.x, centre.x + 1):
            # y  = y1 + (x - x1)/m
            y = centre.y + dy * (x - centre.x)/dx
            list_of_points.append(Point(x, y))
    # logging.debug("theta: %.2f, Number of points: %d" % (theta, len(list_of_points)))

    return list_of_points


def get_point_at_distance(theta: float, radius: int, origin=Point(0, 0)):
    # Create point from the origin
    target = Point()

    if theta == 0:
        target.x = origin.x + radius
        target.y = origin.y
    elif theta == 90:
        target.x = origin.x
        target.y = origin.y + radius
    elif theta == 180:
        target.x = origin.x + (-1 * radius)
        target.y = origin.y
    elif theta == 270:
        target.x = origin.x
        target.y = origin.y - radius
    elif theta < 180:
        m = math.tan(math.radians(theta))
        dx = radius/(math.sqrt(1+(m*m)))
        dy = m * dx

        target.x = int((origin.x + dx) if theta < 90 else (origin.x - dx))
        target.y = int((origin.y + dy) if theta < 90 else (origin.y - dy))
    else:
        m = math.tan(math.radians(theta))
        dx = radius/(math.sqrt(1+(m*m)))
        dy = m * dx

        target.x = int((origin.x - dx) if theta < 270 else (origin.x + dx))
        target.y = int((origin.y - dy) if theta < 270 else (origin.y + dy))
    # logging.debug("origin: %s, theta: %.2f, radius: %.1f, target: %s" % (origin, theta, radius, target))

    return target
