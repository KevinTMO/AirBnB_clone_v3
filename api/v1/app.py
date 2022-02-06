#!/usr/bin/python3
"""
Module: app.py

Configuring flask for our app
"""

from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, make_response
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tearApp(self):
    """
    closing session query
    """
    storage.close()


@app.errorhandler(404)
def pageNotFound(error):
    """
    Handlers errors 404
    """
    return make_response(jsonify({
        'error': 'Not found'
    }), 404)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
