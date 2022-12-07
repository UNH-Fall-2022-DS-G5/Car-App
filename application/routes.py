from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd
import json

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/carclassify", methods=['GET', 'POST'])
def carclassify():

    #extract form inputs
    buying = request.form.get("buying")
    maint = request.form.get("maint")
    doors = request.form.get("doors")
    persons = request.form.get("persons")
    lug_boot = request.form.get("lug_boot")
    safety = request.form.get("safety")

    #extract data from json
    input_data = json.dumps({"buying": buying, "maint": maint, "doors": doors, "persons": persons, "lug_boot": lug_boot, "safety": safety})

    #url for car classification api
    url = "http://127.0.0.1:8000/api"
    #url = "https://dsm-car-model.herokuapp.com/api"

 
    #post data to url
    results =  requests.post(url, input_data)
    content =results.content.decode('UTF-8')
    content=json.loads(content)
    print (content['Prediction'])
    #send input values and prediction result to index.html for display
    return render_template("index.html", buying = buying, maint = maint, doors = doors, persons = persons, lug_boot = lug_boot, safety = safety, results=results.content)
  
