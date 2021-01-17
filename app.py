# Dependencies
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# create engine to hawaii.sqlite
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask
app = Flask(__name__)

@app.route("/")
def home():
    return (
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/start (enter as YYYY-MM-DD)<br/>'
        f'/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)''

    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    results = session.query(Measurement).all()

    prcp = []
    for result in results:
            prcp_dict = {}
		    prcp_dict["date"] = result.date
		    prcp_dict["prcp"] = result.prcp
		    prcp.append(year_prcp_dict)
    return jsonify(prcp)

@app.route('/api/v1.0/Station')
def stations():
    results = session.query(Station.station).all()
    list_stations = list(np.ravel(results))
    return jsonify(list_stations)

@app.route('/api/v1.0/tobs')
def temp():
        last_year = dt.date(2017,8,23) - dt.timedelta(days=365)

        temp_resul
