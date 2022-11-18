#!/usr/bin/env python3
"""Mini-Project3: shows proficiency with flask.
   Creating an API.
   Author: Dorian Majano"""

# Import the functions needed to serve JSON data
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

# Create a Flask instance
app= Flask(__name__)

# Create my data structure
data= [{
    "band": "The Black Keys",
    "category": "Rock",
    "members": [
        "Dan Auerbach",
        "Patrick Carney"
    ],
    "albums": [
        { "name": "The Big Come Up", "releaseYear": 2002 },
        { "name": "Thickfreakness", "releaseYear": 2003 },
        { "name": "Rubber Factory", "releaseYear": 2004 },
        { "name": "Magic Potion", "releaseYear": 2006 },
        { "name": "Attack & Release", "releaseYear": 2008 },
        { "name": "Brothers", "releaseYear": 2010 },
        { "name": "El Camino", "releaseYear": 2011 },
        { "name": "Turn Blue", "releaseYear": 2014 },
        { "name": "'Let's Rock'", "releaseYear": 2019 },
        { "name": "Delta Kream", "releaseYear": 2021 },
        { "name": "Dropout Boogie", "releaseYear": 2022 }
    ],
}]

# Create route to GET bands
@app.route("/bands")
def bands():
    # jsonify returns legal JSON
    return jsonify(data)

# Create route to POST bands
@app.route("/create/bands", methods=["POST"])
def createBands():
    if request.method == 'POST':
        req = request.json
        if req:
            req = json.loads(req)
            band = req["band"]
            category = req["category"]
            members = req["members"]
            albums = req["albums"]
            data.append({"band":band,"category":category,"members":members,"albums":albums})

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

