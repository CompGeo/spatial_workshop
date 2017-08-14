import json
from .crossing_number import point_in_polygon


class PointProcessor:
    polygon_path = 'static/deu.geojson'
    points_path = 'static/points.geojson'
    processed_path = 'static/pointsprocessed.geojson'
    polygon = None
    points = None

    def __init__(self, polygon_path=None, points_path=None, processed_path=None):
        if polygon_path is not None:
            self.polygon_path = polygon_path
        self.load_polygon()

        if points_path is not None:
            self.points_path = points_path
        self.load_points()

        if processed_path is not None:
            self.processed_path = processed_path

    def load_polygon(self):
        with open(self.polygon_path) as geojson:
            self.polygon = json.load(geojson)

    def load_points(self):
        with open(self.points_path) as geojson:
            self.points = json.load(geojson)

    def write_processed(self):
        with open(self.processed_path, 'w') as out:
            json.dump(self.points, out)

    def process(self):

        features = self.points['features']
        # for each point in points, find the crossing number, set property 'in_polygon' to true or false
        polygon_points = self.polygon['features'][0]['geometry']['coordinates'][0]

        for f in features:
            if point_in_polygon(polygon_points, f['geometry']['coordinates']):
                f['properties']['in_polygon'] = True
            else:
                f['properties']['in_polygon'] = False

        self.write_processed()
        return self.points


