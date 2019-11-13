import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from utils import database
import urllib2, json

app = Flask(__name__)

## homepage
@app.route("/")
def start():
    return render_template('main.html')

## mood graph over time
@app.route("/mood_graph")
def graph():
    return render_template('moodgraph.html', mood = database.getMoods())

## gratitude journal
@app.route("/journal")
def get_journal():
    return render_template('journal.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
