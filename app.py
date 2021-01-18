#kcharlesr

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
        print('Routes available:')
        return (
            f'Available Routes:<br/>'
            f'/api/v1.0/precipitation<br/>'
            f'/api/v1.0/stations<br/>'
            f'/api/v1.0/tobs<br/>'
            f'/api/v1.0/start (enter as YYYY-MM-DD)<br/>'
            f'/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)'

    )

@app.route('/api/v1.0/precipitation')
def precipitation():
        results = session.query(Measurements.date,Measurements.prcp).filter(Measurements.date >= "08-23-2017").all()

        # prcp = []
        # for result in results:
        #         prcp_dict = {}
	# 	prcp_dict[Measurements.date] = prcp_dict[Measurements.prcp]
	# 	prcp.append(prcp_dict)
        
        # return jsonify(prcp)
        
@app.route('/api/v1.0/Station')
def stations():
        results = session.query(Station.station).all()
        stations = []
        list_stations = list(np.ravel(results))
        
        return jsonify(list_stations)


@app.route('/api/v1.0/tobs')
def temperature():
        last_year = dt.date(2017,8,23) - dt.timedelta(days=365)
        
        results = session.query(Measurement.tobs).filter(Measurement.date > last_year).all()
        
        tobs = []
        tobs = list(np.ravel(temp_results))

        return jsonify(tobs)


@app.route('/api/v1.0/<start>')
def start_only(start):
        start_date = dt.datetime.strptime(start,'%Y-%m-%d')
        
        summary_data = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.round(func.avg(Measurement.tobs))).\
        filter(Measurement.date >= start_date).all()
        summary = list(np.ravel(summary_data))
        
        return jsonify(summary)

        
@app.route('/api/v1.0/<start>/<end>')
def start_end(start,end):
        start_date = dt.datetime.strptime(start,'%Y-%m-%d')
        end_date = dt.datetime.strptime(end,'%Y-%m-%d' )

        summary_data = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.round(func.avg(Measurement.tobs))).\
        filter(Measurement.date.between(Start_Date,End_Date)).all()
        summary = list(np.ravel(summary_data))

        return jsonify(summary)

if __name__ == "__main__":
	app.run(debug=True)