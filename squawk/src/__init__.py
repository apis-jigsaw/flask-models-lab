from flask import Flask
from .db import get_db
from .orm import *

import simplejson as json


def create_app(database='foursquare_development', testing = False, debug = True):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=database,
        DEBUG = debug,
        TESTING = testing
    )

    return app


