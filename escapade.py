from flask import Flask
from flask import render_template
from flask import request
import osm_parser as osm
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/planner/")
def newplan():
    return render_template('planner.html')

@app.route("/planner/<int:plan_id>")
def get_plan(plan_id):
    return render_template('planner.html', plan=plan_id)

@app.route("/query/", methods=["POST"])
def make_query():
    points = osm.build_query(**request.form)
    return points
