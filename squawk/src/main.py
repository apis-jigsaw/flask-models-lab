from flask import Flask, jsonify
import psycopg2
from venue import Venue
from category import Category

app = Flask(__name__)


@app.route('/venues')
def venues():
    conn = psycopg2.connect(database = 'foursquare_development', user = 'postgres', password = 'postgres')
    cursor = conn.cursor()
    pass    

app.run(debug = True)