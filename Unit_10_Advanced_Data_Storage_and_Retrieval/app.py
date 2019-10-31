import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources\hawaii.sqlite")
#                                  C:\Users\tammy\Documents\Donald_SMU_Data_Science_Bootcamp\wk_10_Advanced_Data_Storage_and_Retrieval\Resources
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################

app= Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route('/')
def origin():
    return(
        f'Welcome to the Weather API!<br/>'
        f'<br/>'
        f'Precipitation data /api/precipitation'
        f'<br/>'
        f'Station data /api/stations'
        f'<br/>'
        f'Temperature data /api/tobs'
        f'<br/>'
        f'Start date & Years /api/<start>  ***'
        f'<br/>'
        f'End date /api/<start>/<end>  ***'
        f'<br/>'
        f'*** Please note dates in the following format are accepted:<br/>'
        f'05052016  =  05/05/2016'
    )
@app.route('/api/precipitation')
def precipitation():
    session = Session(engine)
    prec = session.query(Measurement.date, Measurement.prcp).group_by(Measurement.date).all()
    results = list(np.ravel(prec))
    session.close()
    return jsonify(results)
@app.route('/api/stations')
def stations():
    session = Session(engine)
    stations = session.query(Measurement.station).group_by(Measurement.station).all()
    results = list(np.ravel(stations))
    session.close()
    return jsonify(results)
@app.route('/api/tobs')
def tobs():
    session = Session(engine)
    tobs = session.query(Measurement.date, Measurement.tobs).group_by(Measurement.date).all()
    results = list(np.ravel(tobs))
    session.close()
    return jsonify(results)
@app.route('/api/<start>')
def start(start):
    session = Session(engine)
    begin=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), 
        func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    results = list(np.ravel(begin))
    session.close()
    return jsonify(results)
@app.route('/api/<start>/<end>')
def end(start, end):
    session = Session(engine)
    begin = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), 
    func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    results = list(np.ravel(begin))
    session.close()
    return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)