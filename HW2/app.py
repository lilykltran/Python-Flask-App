# Lily Tran- Cloud Systems Fall 2019 - HW2

from flask import Flask, render_template
import flask.views
import requests

from model import DModel

app = Flask(__name__)
model = DModel(app)

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/bubbletea')
def bubbletea():
  bubbletea = model.fetchall()
  return render_template("bubbletea.html", bubbletea=bubbletea)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 8000, debug=True)
