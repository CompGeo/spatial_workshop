import json
from collections import deque
from .utilities import test_ccw


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
            # TODO: implement this step

            while Melkman.in_left(new_point, d):
                # TODO: replace 'pass' with pop from the deque... which end?
                pass

            # TODO: append the new_point to the deque... which end?

            while Melkman.in_right(new_point, d):
                # TODO: replace 'pass' with pop from the deque... which end?
                pass

            # TODO: append the new_point to the deque... which end?

        self.hull = Melkman.deque_to_geojson(d)
        self.write_hull()
        return self.hull

    @staticmethod
    def initialize_deque(pt1, pt2, pt3):
        """
        initialize the double-ended queue. remember that the last point should be at both 
        the top and bottom of the deque. the initialized deque should hold a convex hull of the
        first 3 points in CCW winding order.
        :param pt1: 
        :param pt2: 
        :param pt3: 
        :return: deque object
        """
        d = deque()
        raise Exception("implement me!")
        return d

    @staticmethod
    def inside_hull(pt, dq):
        """
        hint: this is the 'and' of 2 test_ccw tests
        :param pt: 
        :param dq: 
        :return: 
        """
        return True

    @staticmethod
    def in_right(pt, dq):
        """
        hint: 1 test_ccw test. include the co-linear condition
        :param pt: 
        :param dq: 
        :return: 
        """
        return True

    @staticmethod
    def in_left(pt, dq):
        """
        hint: 1 test_ccw test. include the co-linear condition. which end of the deque?
        :param pt: 
        :param dq: 
        :return: 
        """
        return True

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

