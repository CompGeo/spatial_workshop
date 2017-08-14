#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_even(num):
    return num % 2 == 0


def upward_crossing(p1, p2, test_point):
    """
    test to determine if the segment defined by p1 and p2 crosses the horizontal ray in an upward direction
    remember: an upward edge includes its starting endpoint, and excludes its final endpoint
    :param p1: 
    :param p2: 
    :param test_point: 
    :return: boolean
    """
    raise Exception("Implement me!")
    return True


def downward_crossing(p1, p2, test_point):
    """
    test to determine if the segment defined by p1 and p2 crosses the horizontal ray in an downward direction
    remember: a downward edge excludes its starting endpoint, and includes its final endpoint 
    :param p1: 
    :param p2: 
    :param test_point: 
    :return: boolean
    """
    raise Exception("Implement me!")
    return True


def x_crossing(p1, p2, test_point):
    """
    compute the actual edge-ray intersect x-coordinate.
    look at screen for a reminder of how to get the equation of a line from 2 points
    :param p1: 
    :param p2: 
    :param test_point: 
    :return: x coordinate of the edge-ray intersection
    """
    x_val = None
    raise Exception("Implement me!")
    return x_val


def crossing_number(polygon_points, test_point):
    cn = 0  # crossing number counter

    # loop through consecutive segments in the polygon
    for i in range(0, len(polygon_points) - 1):
        # TODO: fill in the expressions for point1 and point2. they should be lists of the form [x,y]
        point1 = None
        point2 = None
        # TODO: implement upward_crossing and downward_crossing
        # (HINT: do you need both coordinate values for each pair to determine this?)
        up_cross = upward_crossing(point1, point2, test_point)
        down_cross = downward_crossing(point1, point2, test_point)

        # We've tested for the edge crossing a horizontal line, but we still need to test if the crossing is strictly
        # to the right of the test point
        if up_cross or down_cross:
            # compute the actual edge-ray intersect x-coordinate, so we can compare with the test point
            # TODO: implement x_crossing
            if test_point[0] < x_crossing(point1, point2, test_point):
                cn += 1

    return cn


def point_in_polygon(polygon_points, test_point):
    return not is_even(crossing_number(polygon_points, test_point))
