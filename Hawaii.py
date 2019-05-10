
#!/usr/bin/env python
# coding: utf-8


import sqlite3
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)
conn = sqlite3.connect("Resources/hawaii.sqlite")
cur = conn.cursor()

#cur.execute
#obtain data from cursor via loop 
#rows = cur.fetchall()
 
#for row in rows:
#   print(row)


@app.route("/")
def home():
    """List all available api routes."""
    return ("Available Routes:<br>\n/api/v1.0/precipitation<br>\n/api/v1.0/stations<br>\n/api/v1.0/tobs<br>\n/api/v1.0/startdate<br>\n/api/v1.0/startdate/enddate")

    # Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("select date, prcp from measurement Where date >= Date((Select max(date) from measurement),'-12 months') order by date asc")  
    rows = cur.fetchall()
    column_list = []
    prcp_list =[]
    for row in rows: 
        column_list.append(row[0])
        prcp_list.append(row[1])
  
    columndata = dict()
    columndata["date"] = column_list
    columndata["prcp"] = prcp_list
    return jsonify(columndata)

    # Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT station FROM station")  
    rows = cur.fetchall()
    column_list = []
    for row in rows: 
        column_list.append(row[0])
  
    columndata = dict()
    columndata["station"] = column_list
    return jsonify(columndata)

    # query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("select date, tobs from measurement Where date >= Date((Select max(date) from measurement),'-12 months')  order by date asc")  
    rows = cur.fetchall()
    date_list = []
    tobs_list =[]
    for row in rows: 
        date_list.append(row[0])
        tobs_list.append(row[1])
  
    columndata = dict()
    columndata["date"] = date_list
    columndata["tobs"] = tobs_list
    return jsonify(columndata)

    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.



@app.route("/api/v1.0/<start>")
def calc_temps(start_date):
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("select min(tobs) as 'min', max(tobs) as 'max', avg(tobs) as 'avg' from measurement where date >= '" + str(start_date) + "' order by date asc")  
    rows = cur.fetchall()
    min_list =[]
    max_list =[]
    avg_list = []
    for row in rows: 
        min_list.append(row[0])
        max_list.append(row[1])
        avg_list.append(row[2])
  
    columndata = dict()
    columndata["min_temp"] = min_list
    columndata["max_temp"] = max_list
    columndata["avg_temp"] = avg_list
    return jsonify(columndata)

@app.route("/api/v1.0/<start>/<end>")
def calc_temps2(start_date,end_date):
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("select min(tobs) as 'min', max(tobs) as 'max', avg(tobs) as 'avg' from measurement where date between " +str(start_date)+ " and " + str(end_date) +" order by date asc")  
    rows = cur.fetchall()
    min_list =[]
    max_list =[]
    avg_list = []
    for row in rows: 
        min_list.append(row[0])
        max_list.append(row[1])
        avg_list.append(row[2])
  
    columndata = dict()
    columndata["min_temp"] = min_list
    columndata["max_temp"] = max_list
    columndata["avg_temp"] = avg_list
    return jsonify(columndata)


if __name__ == '__main__':
    app.run(debug=True)