from flask import Flask, current_app, jsonify
from process_points_cn import PointProcessor
from melkman import Melkman
from triangulate_polygon import TriangulatePolygon
from triangulate_points import TriangulatePoints
app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask is running!"


@app.route("/pointlocation")
def pointlocation():
    return current_app.send_static_file('pointlocation.html')


@app.route("/pip")
def point_in_polygon():
    p = PointProcessor()
    return jsonify(p.process())


@app.route("/convexhull")
def convexhull():
    return current_app.send_static_file('convexhull.html')


@app.route("/convexhullfrompolygon")
def convexhullfrompolygon():
    m = Melkman()
    return jsonify(m.process())


@app.route("/fan")
def fan():
    return current_app.send_static_file('triangulatepoly.html')


@app.route("/triangulatepolygon")
def triangulatepolygon():
    t = TriangulatePolygon()
    return jsonify(t.process())


@app.route("/triangulation")
def full_triangulation():
    return current_app.send_static_file('triangulatepoints.html')


@app.route("/triangulatepoints")
def triangulatepoints():
    t = TriangulatePoints()
    return jsonify(t.process())

@app.route('/static/<string:page_name>')
def static_page(page_name):
    return current_app.send_static_file(page_name)
