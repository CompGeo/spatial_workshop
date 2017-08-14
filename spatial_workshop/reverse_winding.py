import json


class ReverseWinding:
    polygon_path = 'static/deu.geojson'
    polygon = None

    def __init__(self, polygon_path=None):
        if polygon_path is not None:
            self.polygon_path = polygon_path
        self.load_polygon()

    def load_polygon(self):
        with open(self.polygon_path) as geojson:
            self.polygon = json.load(geojson)

    def write_polygon(self):
        with open(self.polygon_path, 'w') as out:
            json.dump(self.polygon, out)

    def process(self):
        # get the points (x,y) from the geojson object
        self.polygon['features'][0]['geometry']['coordinates'][0].reverse()
        self.write_polygon()
        return self.polygon
