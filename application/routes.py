from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/bankclassify", methods=['GET', 'POST'])
def bankclassify():

    #extract form inputs
    ticker_value = request.form.get("ticker")


   #convert data to json
    input_data = json.dumps({"ticker": ticker_value})

    #url for bank marketing model
    url = "http://localhost:5000/api"
    #url = "https://bank-model-app.herokuapp.com/api"
  
    #post data to url
    results =  requests.post(url, input_data)
    #send input values and prediction result to index.html for display
    return render_template("index.html", ticker = ticker_value,  results= results.content.decode('UTF-8'))
    #return results