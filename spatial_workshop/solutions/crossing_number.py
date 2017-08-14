
def is_even(num):
    return num % 2 == 0


def upward_crossing(p1, p2, test_point):
    return p1[1] <= test_point[1] and p2[1] > test_point[1]


def downward_crossing(p1, p2, test_point):
    return p1[1] > test_point[1] and p2[1] <= test_point[1]


def x_crossing(p1, p2, test_point):
    vt = (test_point[1] - p1[1]) / (p2[1] - p1[1])
    x_val = p1[0] + vt * (p2[0] - p1[0])
    return x_val


def crossing_number(polygon_points, test_point):
    cn = 0  # crossing number counter

    # loop through consecutive segments in the polygon
    for i in range(0, len(polygon_points) - 1):
        point1 = polygon_points[i]
        point2 = polygon_points[i + 1]
        up_cross = upward_crossing(point1, point2, test_point)
        down_cross = downward_crossing(point1, point2, test_point)
        if up_cross or down_cross:
            # compute the actual edge-ray intersect x-coordinate, compare with the test point
            if test_point[0] < x_crossing(point1, point2, test_point):
                cn += 1

    return cn


def point_in_polygon(polygon_points, test_point):
    return not is_even(crossing_number(polygon_points, test_point))
