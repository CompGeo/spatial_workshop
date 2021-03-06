import json
from .utilities import test_ccw


class TriangulatePolygon:
    hull_path = 'static/hull.geojson'
    hull = None

    tri_path = 'static/tri_polygon.geojson'
    tri = None

    def __init__(self, hull_path=None, tri_path=None):
        if hull_path is not None:
            self.hull_path = hull_path

        self.load_hull()

        if tri_path is not None:
            self.tri_path = tri_path

    def load_hull(self):
        with open(self.hull_path) as geojson:
            self.hull = json.load(geojson)

    def write_tri(self):
        with open(self.tri_path, 'w') as out:
            json.dump(self.tri, out)

    def process(self):
        # get the points (x,y) from the hull geojson object

        # fan triangulation of a convex polygon

        # write each triangle as a geojson 'Feature'

        self.write_tri()
        return self.tri

    @staticmethod
    def geojson_skeleton():
        return {
            'type': 'FeatureCollection',
            'features': []
        }

    @staticmethod
    def feature_skeleton(coord_arr):
        return {
            'type': 'Feature',
            'properties': {'name': 'triangulation'},
            'geometry': {
                'type': 'Polygon',
                'coordinates': [coord_arr]
            }

        }
