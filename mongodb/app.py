#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import sys
import os

from flask import Flask
app = Flask(__name__)

DEFAULT_PORT = 2001


client = MongoClient()

def find_restuarant( zipcode):
    results = []
    db = client.test
    cur = db.restaurants.find( {"address.zipcode": zipcode})
    for doc in cur:
        results.append( doc)

def get_port():
    if not os.environ['FLASK_PORT']:
        return DEFAULT_PORT
    else:
        return int( os.environ['FLASK_PORT'])

@app.route("/")
def hello():
    return find_restuarant( "10075")


if __name__ == "__main__":
    app.run( host='0.0.0.0', port=get_port(), debug=True)
