from flask import Flask, jsonify

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

from datetime import datetime

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect = True)

Measurements = Base.classes.measurements
Stations = Base.classes.stations

session = Session(engine)

##### Set up Flask
app = Flask(__name__)

#home route
@app.route("/")
def home():
    return ("Hawaii Weather Data API<br/>"
            "/api/v1.0/precipitation<br/>"
            "/api/v1.0/stations<br/>"
            "/api/v1.0/tobs<br/>"
            "/api/v1.0/yyyy-mm-dd/<br/>"
            "/api/v1.0/yyyy-mm-dd/yyyy-mm-dd/")

