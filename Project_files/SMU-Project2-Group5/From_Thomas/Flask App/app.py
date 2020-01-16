from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import sqlite3

import pandas as pd

# Database Setup
engine = create_engine("sqlite:///RSPO_mills.sqlite")

app = Flask(__name__)

@app.route('/')
def Home():
   
    return render_template('index.html')

@app.route('/data')
def data():
    conn = engine.connect()

    query = f"""SELECT * FROM 'RSPO_mills' LIMIT 100
            """
            
    #execute query
    df = pd.read_sql(query, conn) 

    #debug log to console
    print(df.head(10))

    #close db connection
    conn.close()
    return df.to_json(orient="index")

@app.route('/analytics')
def Analytics():
    return render_template('analytics.html')

@app.route('/line')
def Line():
    return render_template('line.html')

@app.route('/markers')
def Markers():
    return render_template('markers.html')

@app.route('/about')
def About():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)