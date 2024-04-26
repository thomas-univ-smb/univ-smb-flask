# save this as app.py
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def template():
    return render_template('template.html')

@app.route("/start")
def start():
    return render_template('start.html')

@app.route("/rules_filter")
def rules_filter():
    return render_template('rules_filter.html')

@app.route("/rules_nat")
def rules_nat():
    return render_template('rules_nat.html')

@app.route("/rules_nat_add")
def rules_net_add():
    return render_template('rules_nat_add.html')

@app.route("/alias")
def alias():
    f = open('static/alias.json')
    data = json.load(f) 
    f.close()
    return render_template('alias.html', summary = data)
