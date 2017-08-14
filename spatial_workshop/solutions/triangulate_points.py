import json
from copy import deepcopy
from crossing_number import point_in_polygon
from utilities import test_ccw


class TriangulatePoints:
    tri_path = 'static/tri_polygon.geojson'
    tri = None

    points_path = 'static/pointsprocessed.geojson'
    points = None

    fulltri_path = 'static/triangulation.geojson'
    fulltri = None

    def __init__(self, tri_path=None, points_path=None, fulltri_path=None):
        if tri_path is not None:
            self.tri_path = tri_path

        self.load_tri()

        if points_path is not None:
            self.points_path = points_path

        self.load_points()

        if fulltri_path is not None:
            self.fulltri_path = fulltri_path

    def load_tri(self):
        """
        load the polygon triangulation (fan)
        :return: 
        """
        with open(self.tri_path) as geojson:
            self.tri = json.load(geojson)

    def load_points(self):
        """
        load the points we processed earlier. we will add the interior points to the triangulation
        :return: 
        """
        with open(self.points_path) as geojson:
            self.points = json.load(geojson)

    def write_fulltri(self):
        """
        write the full triangulation geojson object to a file, so we can use it later
        :return: 
        """
        with open(self.fulltri_path, 'w') as out:
            json.dump(self.tri, out)

    def process(self):
        # get the points (x,y) from the geojson object
        pts = self.points['features']

        # iterate over all the points
        for p in pts:
            if not p['properties']['in_polygon']:
                # skip points not in the polygon
                continue

            triangles = self.tri['features']
            for t in triangles:
                # avoid any referencing issues for clarity
                geom = deepcopy(t['geometry']['coordinates'][0])
                add_point = deepcopy(p['geometry']['coordinates'])
                if point_in_polygon(geom, add_point):
                    # if the point is in the triangle, we have to remove the matched triangle,
                    # then create new sub triangles
                    new_triangles = TriangulatePoints.decompose_triangle(geom, add_point)
                    for nt in new_triangles:
                        triangles.append(nt)
                    triangles.remove(t)
                    break

        self.write_fulltri()
        return self.tri

    @staticmethod
    def decompose_triangle(triangle, point):
        """
        given a triangle and a point (within the triangle), decompose the triangle into 3 triangles. 
        :param triangle: 
        :param point: 
        :return: 
        """
        features = []
        for i in range(0, len(triangle) - 1):
            if test_ccw(point, triangle[i], triangle[i + 1]) > 0:
                new_tri = [point, triangle[i], triangle[i + 1], point]
            else:
                new_tri = [point, triangle[i + 1], triangle[i], point]
            features.append(TriangulatePoints.feature_skeleton(new_tri))
        return features

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
            'properties': {'name': 'full_triangulation'},
            'geometry': {
                'type': 'Polygon',
                'coordinates': [coord_arr]
            }

        }
