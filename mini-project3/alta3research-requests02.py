#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/bands"

resp= requests.get(URL).json()

pprint(resp)

print()

URL= "http://127.0.0.1:2224/create/bands"

band = {
            "band": "Kings of Leon",
            "category": "Rock",
            "members": [
                "Caleb Followill",
                "Jared Followill",
                "Matthew Followill",
                "Nathan Followill"
            ],
            "albums": [
                { "name": "Youth & Young Manhood", "releaseYear": 2003 },
                { "name": "Aha Shake Heartbreak", "releaseYear": 2004 },
                { "name": "Because of the Times", "releaseYear": 2007 },
                { "name": "Only by the Night", "releaseYear": 2008 },
                { "name": "Come Around Sundown", "releaseYear": 2010 },
                { "name": "Mechanical Bull", "releaseYear": 2013 },
                { "name": "Walls", "releaseYear": 2016 },
                { "name": "When You See Yourself", "releaseYear": 2021 }
            ]
        }

band = json.dumps(band)

res = requests.post(URL, json=band)

# pprint(res.json())
print(res.json())
