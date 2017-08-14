import json
from collections import deque
from utilities import test_ccw


class Melkman:
    polygon_path = 'static/deu.geojson'
    hull_path = 'static/hull.geojson'
    polygon = None
    hull = None

    def __init__(self, polygon_path=None, hull_path=None):
        if polygon_path is not None:
            self.polygon_path = polygon_path
        self.load_polygon()

        if hull_path is not None:
            self.hull_path = hull_path

    def load_polygon(self):
        with open(self.polygon_path) as geojson:
            self.polygon = json.load(geojson)

    def write_hull(self):
        with open(self.hull_path, 'w') as out:
            json.dump(self.hull, out)

    def process(self):
        # get the points (x,y) from the geojson object
        pts = self.polygon['features'][0]['geometry']['coordinates'][0]

        # set up the deque with the initial convex hull, ccw winding
        d = Melkman.initialize_deque(pts[0], pts[1], pts[2])

        # add the rest of the points

        for i in range(3, len(pts) - 1):
            new_point = pts[i]
            # test the new point to determine how to update the deque

            # if the new point is inside the current hull, skip it
            if Melkman.inside_hull(new_point, d):
                # print("inside hull")
                continue

            while Melkman.in_left(new_point, d):
                d.pop()
            d.append(new_point)

            while Melkman.in_right(new_point, d):
                d.popleft()
            d.appendleft(new_point)

        self.hull = Melkman.deque_to_geojson(d)
        self.write_hull()
        return self.hull

    @staticmethod
    def initialize_deque(pt1, pt2, pt3):
        d = deque()
        if test_ccw(pt1, pt2, pt3) > 0:
            d.append(pt3)
            d.append(pt1)
            d.append(pt2)
            d.append(pt3)
        else:
            d.append(pt3)
            d.append(pt2)
            d.append(pt1)
            d.append(pt3)
        return d

    @staticmethod
    def inside_hull(pt, dq):
        return test_ccw(dq[0], dq[1], pt) > 0 and test_ccw(dq[-2], dq[-1], pt) > 0

    @staticmethod
    def in_right(pt, dq):
        return test_ccw(dq[0], dq[1], pt) <= 0

    @staticmethod
    def in_left(pt, dq):
        return test_ccw(dq[-2], dq[-1], pt) <= 0

    @staticmethod
    def deque_to_geojson(hull_deque):
        hull = Melkman.geojson_skeleton()
        hull_points = hull['features'][0]['geometry']['coordinates'][0]
        for val in hull_deque:
            hull_points.append(val)
        return hull

    @staticmethod
    def geojson_skeleton():
        gj = {
            'type': 'FeatureCollection',
            'features': [{
                'type': 'Feature',
                'properties': {'name': 'convex_hull'},
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [[]]
                }

            }]
        }
        return gj

