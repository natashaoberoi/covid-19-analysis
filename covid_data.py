{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b25aa8e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import urllib.request,urllib.parse, urllib.error, json \n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly.graph_objects as go"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05830139",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a set of tables in SQLite DB\n",
    "conn = sqlite3.connect('covid_data.sqlite')\n",
    "cur = conn.cursor()\n",
    "\n",
    "cur.executescript('''\n",
    "CREATE TABLE IF NOT EXISTS states (\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, \n",
    "    state TEXT UNIQUE, \n",
    "    abbreviation TEXT\n",
    ");\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS covid_data (\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, \n",
    "    group_by TEXT, \n",
    "    state_id INTEGER FOREIGN KEY REFERENCES states(id), \n",
    "    condition_group TEXT, \n",
    "    condition TEXT, \n",
    "    age_group TEXT, \n",
    "    covid_19_deaths INTEGER, \n",
    "    number_of_mentions INTEGER\n",
    ");\n",
    "\n",
    "CREATE TABLE IF NOT EXISTS vaccine_data (\n",
    "    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,\n",
    "    state_id INTEGER FOREIGN KEY REFERENCES states(id),\n",
    "    number_of_vaccines INTEGER\n",
    ");''')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
