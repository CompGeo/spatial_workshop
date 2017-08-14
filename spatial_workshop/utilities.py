
def test_ccw(p0, p1, p2):
    """
    cross product. 
    :param p0: point 1
    :param p1: point 2
    :param p2: point 3
    :return: >0 for p2 left of the line through p0 and p1, =0 for p2 on the line, <0 for 23 right of the line
    """
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


def circumcenter(a, b, c):
    """
    Return the center of the circumscribed circle of triangle abc.
    # Taken from https://www.ics.uci.edu/~eppstein/junkyard/circumcenter.html
    :param a: 
    :param b: 
    :param c: 
    :return: 
    """
    xa = a[0]
    ya = a[1]
    xb = b[0]
    yb = b[1]
    xc = c[0]
    yc = c[1]
    d = 2 * ((xa - xc) * (yb - yc) - (xb - xc) * (ya - yc))
    ka = ((xa - xc) * (xa + xc) + (ya - yc) * (ya + yc))
    kb = ((xb - xc) * (xb + xc) + (yb - yc) * (yb + yc))
    xp = ka * (yb - yc) - kb * (ya - yc)
    yp = kb * (xa - xc) - ka * (xb - xc)
    return [xp / d, yp / d]


def dist_sq (u, v):
    dx = u[0] - v[0]
    dy = u[1] - v[1]
    return dx * dx + dy * dy;


def point_in_circumcircle(a, b, c, v):
    """
    Check whether v is strictly in the interior of the circumcircle of the triangle abc.
    
    :param a: 
    :param b: 
    :param c: 
    :param v: 
    :return: 
    """
    p = circumcenter(a, b, c)
    return dist_sq(p, v) < dist_sq(a, p)
