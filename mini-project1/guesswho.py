#!/usr/bin/python3
"""Guess who, Bob's burgers edition
    Author: Dorian Majano"""

import random

## Requirements: use conditionals to return unique values based on user input
## Include at least 1 loop 
## Include error handling as best as possible

# Create a list of dictionaries to store the characters from Bob's burgers
# Attributes will include: name, sex, hair color, age, glasses?,
characters = [
        {"name": "Bob",    "sex": "male",   "hair": "black", "glasses": False}, 
        {"name": "Linda",  "sex": "female", "hair": "black", "glasses": True}, 
        {"name": "Tina",   "sex": "female", "hair": "black", "glasses": True}, 
        {"name": "Gene",   "sex": "male",   "hair": "black", "glasses": False}, 
        {"name": "Louise", "sex": "female", "hair": "black", "glasses": False}, 
        {"name": "Teddy",  "sex": "male",   "hair": "bald",  "glasses": False}, 
        ]

guesswho = characters[random.randrange(characters.__len__())]['name']

print(guesswho)
