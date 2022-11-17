#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

# This is the landing page for users, answers will be posted here
@app.route("/")
def trivia():
    return render_template("trivia.html")

# This is where we want to redirect users if the answer is correct
@app.route("/correct")
def correct():
    return "Correct!"

@app.route("/answer", methods = ["POST"])
def answer():
    page = ''
    if request.method == "POST":
        if request.form.get("answer") == "42":
            page = redirect(url_for("correct"))
        else:
            page = redirect(url_for("trivia"))

    return page

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

