from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker
from config import username, password, db_name
from flask import Flask, jsonify, Response
from sqlalchemy.orm import Session
import pandas as pd
import sqlalchemy
from datetime import datetime

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@localhost:5432/{db_name}')
connection = engine.connect()
db = scoped_session(sessionmaker(bind=engine))

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<b>Available Routes:</b><br>"
        f"1. <a href=\"/vaccines\">Current Vaccination Figures</a>: (/vaccines)<br/>"
        f"2. <a href=\"/cases\">All Case Data in 2021</a>: (/cases)<br/>"
        f"3. <a href=\"/country_metadata\">Individual country metrics as of 01/03/2022</a>: (/country_metadata)<br/>"
        f"4. <a href=\"/region_metadata\">Individual region metrics as of 01/03/2022</a>: (/country_metadata)<br/>"
        f"5. <a href=\"/cases_filtered\">Filtered 2021 case data</a>: (/cases_filtered)<br/>"
    )


@app.route("/vaccines")
def vaccines():
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    """Return a list of vaccine data, containing individual country metrics"""
    # Query all vaccines
    results = pd.read_sql(f"SELECT * FROM vaccines", connection)
    return Response(results.to_json(orient="records",lines=True), mimetype='application/json')

@app.route("/cases")
def cases():
    """Return a list of daily case information in 2021 for all countries"""
    # Query all cases
    results = pd.read_sql(f"SELECT * FROM cases WHERE \"Date_reported\" BETWEEN '2021-12-31' AND '2021-12-31'", connection)
    return Response(results.to_json(orient="records"), mimetype='application/json')

@app.route("/country_metadata")
def country_metadata():
    """Return a list of latest case information for all countries"""
    # Query all cases
    results = pd.read_sql(f"SELECT vaccines.\"Country\", vaccines.\"Alpha-2 code\", vaccines.\"WHO_REGION\", vaccines.\"Latitude\", vaccines.\"Longitude\", vaccines.\"TOTAL_VACCINATIONS\", cases.\"Cumulative_cases\", cases.\"Cumulative_deaths\" FROM vaccines JOIN cases ON vaccines.\"Country\" = cases.\"Country\" WHERE cases.\"Date_reported\" = '2022-01-03'", connection)
    return Response(results.to_json(orient="records"), mimetype='application/json')

@app.route("/region_metadata")
def region_metadata():
    """Return a list of latest case information for all countries"""
    # Query all cases
    results = pd.read_sql(f"SELECT vaccines.\"WHO_REGION\", sum(vaccines.\"TOTAL_VACCINATIONS\") \"TOTAL_VACCINATIONS\", sum(cases.\"Cumulative_cases\") \"Cumulative_cases\", sum(cases.\"Cumulative_deaths\") \"Cumulative_deaths\" FROM vaccines JOIN cases ON vaccines.\"Country\" = cases.\"Country\" WHERE cases.\"Date_reported\" = '2022-01-03' GROUP BY vaccines.\"WHO_REGION\"", connection)
    return Response(results.to_json(orient="records"), mimetype='application/json')

@app.route("/cases_filtered")
def cases_filtered():
    """Return a list of daily case information in 2021 for all countries"""
    # Query all cases
    results = pd.read_sql(f"SELECT \"WHO_region\", \"Date_reported\", sum(\"New_cases\") \"New_cases\", sum(\"New_deaths\") \"New_deaths\" FROM cases WHERE \"Date_reported\" BETWEEN '2021-01-01' AND '2021-12-31' GROUP BY \"WHO_region\", \"Date_reported\" ORDER BY \"Date_reported\"", connection)
    return Response(results.to_json(orient="records", date_format="iso"), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)