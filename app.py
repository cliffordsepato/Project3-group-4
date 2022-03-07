from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import username, password, db_name
from flask import Flask, jsonify, Response
from sqlalchemy.orm import Session
import pandas as pd
import sqlalchemy

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
    )


@app.route("/vaccines")
def vaccines():
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all vaccines
    results = pd.read_sql(f"SELECT * FROM vaccines", connection)
    return Response(results.to_json(orient="records"), mimetype='application/json')

@app.route("/cases")
def cases():
    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all cases
    results = pd.read_sql(f"SELECT * FROM cases WHERE \"Date_reported\" BETWEEN '2021-01-01' AND '2021-01-01'", connection)
    return Response(results.to_json(orient="records"), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)