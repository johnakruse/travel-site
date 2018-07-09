from flask import Flask
from flask import render_template
from flask import request
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

@app.route("/query/")
def make_query():
    points = query(request.form)
    #want to pass a list of nodes, essentially a list of dicts
    return jsonify(points)
