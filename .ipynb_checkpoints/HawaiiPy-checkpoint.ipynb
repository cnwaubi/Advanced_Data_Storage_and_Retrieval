{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "\n",
    "\n",
    "import sqlite3\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "from flask import Flask, jsonify\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "conn = sqlite3.connect(\"Resources/Hawaii.sqlite\")\n",
    "cur = conn.cursor()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#cur.execute\n",
    "#obtain data from cursor via loop \n",
    "#rows = cur.fetchall()\n",
    " \n",
    "#for row in rows:\n",
    "#   print(row)\n",
    "\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    \"\"\"List all available api routes.\"\"\"\n",
    "    return (\"Available Routes:<br>\\n/api/v1.0/precipitation<br>\\n/api/v1.0/stations<br>\\n/api/v1.0/tobs<br>\\n/api/v1.0/startdate<br>\\n/api/v1.0/startdate/enddate\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the query results to a Dictionary using date as the key and prcp as the value.\n",
    "# Return the JSON representation of your dictionary.\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    conn = sqlite3.connect(\"Resources/Hawaii.sqlite\")\n",
    "    cur = conn.cursor()\n",
    "    cur.execute(\"select date, prcp from measurement Where date >= Date((Select max(date) from measurement),'-12 months') order by date asc\")  \n",
    "    rows = cur.fetchall()\n",
    "    column_list = []\n",
    "    prcp_list =[]\n",
    "    for row in rows: \n",
    "        column_list.append(row[0])\n",
    "        prcp_list.append(row[1])\n",
    "  \n",
    "    columndata = dict()\n",
    "    columndata[\"date\"] = column_list\n",
    "    columndata[\"prcp\"] = prcp_list\n",
    "    return jsonify(columndata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Return a JSON list of stations from the dataset.\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    conn = sqlite3.connect(\"Resources/Hawaii.sqlite\")\n",
    "    cur = conn.cursor()\n",
    "    cur.execute(\"SELECT station FROM station\")  \n",
    "    rows = cur.fetchall()\n",
    "    column_list = []\n",
    "    for row in rows: \n",
    "        column_list.append(row[0])\n",
    "  \n",
    "    columndata = dict()\n",
    "    columndata[\"station\"] = column_list\n",
    "    return jsonify(columndata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# query for the dates and temperature observations from a year from the last data point.\n",
    "# Return a JSON list of Temperature Observations (tobs) for the previous year.\n",
    "\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "    conn = sqlite3.connect(\"Resources/Hawaii.sqlite\")\n",
    "    cur = conn.cursor()\n",
    "    cur.execute(\"select date, tobs from measurement Where date >= Date((Select max(date) from measurement),'-12 months')  order by date asc\")  \n",
    "    rows = cur.fetchall()\n",
    "    date_list = []\n",
    "    tobs_list =[]\n",
    "    for row in rows: \n",
    "        date_list.append(row[0])\n",
    "        tobs_list.append(row[1])\n",
    "  \n",
    "    columndata = dict()\n",
    "    columndata[\"date\"] = date_list\n",
    "    columndata[\"tobs\"] = tobs_list\n",
    "    return jsonify(columndata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: Do not use the development server in a production environment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\cnwau\\Anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3304: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.\n",
    "# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.\n",
    "# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.\n",
    "\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/<start>\")\n",
    "def calc_temps(start_date):\n",
    "    conn = sqlite3.connect(\"Resources/Hawaii.sqlite\")\n",
    "    cur = conn.cursor()\n",
    "    cur.execute(\"select min(tobs) as 'min', max(tobs) as 'max', avg(tobs) as 'avg' from measurement where date >= '\" + str(start_date) + \"' order by date asc\")  \n",
    "    rows = cur.fetchall()\n",
    "    min_list =[]\n",
    "    max_list =[]\n",
    "    avg_list = []\n",
    "    for row in rows: \n",
    "        min_list.append(row[0])\n",
    "        max_list.append(row[1])\n",
    "        avg_list.append(row[2])\n",
    "  \n",
    "    columndata = dict()\n",
    "    columndata[\"min_temp\"] = min_list\n",
    "    columndata[\"max_temp\"] = max_list\n",
    "    columndata[\"avg_temp\"] = avg_list\n",
    "    return jsonify(columndata)\n",
    "\n",
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def calc_temps2(start_date,end_date):\n",
    "    conn = sqlite3.connect(\"Resources/Hawaii.sqlite\")\n",
    "    cur = conn.cursor()\n",
    "    cur.execute(\"select min(tobs) as 'min', max(tobs) as 'max', avg(tobs) as 'avg' from measurement where date between \" +str(start_date)+ \" and \" + str(end_date) +\" order by date asc\")  \n",
    "    rows = cur.fetchall()\n",
    "    min_list =[]\n",
    "    max_list =[]\n",
    "    avg_list = []\n",
    "    for row in rows: \n",
    "        min_list.append(row[0])\n",
    "        max_list.append(row[1])\n",
    "        avg_list.append(row[2])\n",
    "  \n",
    "    columndata = dict()\n",
    "    columndata[\"min_temp\"] = min_list\n",
    "    columndata[\"max_temp\"] = max_list\n",
    "    columndata[\"avg_temp\"] = avg_list\n",
    "    return jsonify(columndata)\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mSystemExit\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-c73472191c87>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     48\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     49\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 50\u001b[1;33m     \u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mrun\u001b[1;34m(self, host, port, debug, load_dotenv, **options)\u001b[0m\n\u001b[0;32m    941\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    942\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 943\u001b[1;33m             \u001b[0mrun_simple\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhost\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mport\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    944\u001b[0m         \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    945\u001b[0m             \u001b[1;31m# reset the first request information if the development server\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\werkzeug\\serving.py\u001b[0m in \u001b[0;36mrun_simple\u001b[1;34m(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, reloader_interval, reloader_type, threaded, processes, request_handler, static_files, passthrough_errors, ssl_context)\u001b[0m\n\u001b[0;32m    810\u001b[0m         \u001b[1;32mfrom\u001b[0m \u001b[0mwerkzeug\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_reloader\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mrun_with_reloader\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    811\u001b[0m         run_with_reloader(inner, extra_files, reloader_interval,\n\u001b[1;32m--> 812\u001b[1;33m                           reloader_type)\n\u001b[0m\u001b[0;32m    813\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    814\u001b[0m         \u001b[0minner\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\werkzeug\\_reloader.py\u001b[0m in \u001b[0;36mrun_with_reloader\u001b[1;34m(main_func, extra_files, interval, reloader_type)\u001b[0m\n\u001b[0;32m    273\u001b[0m             \u001b[0mreloader\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    274\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 275\u001b[1;33m             \u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreloader\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrestart_with_reloader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    276\u001b[0m     \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    277\u001b[0m         \u001b[1;32mpass\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mSystemExit\u001b[0m: 1"
     ]
    }
   ],
   "source": [
    "%tb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
