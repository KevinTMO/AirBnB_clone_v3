#!/usr/bin/python3
"""
Module: index.py

Configuring a route to return JSON string

Creating routes:
  - /status: display a string 'status': 'OK'
  - /stats: display the count of all clases objects
"""


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """
    return a JSON string: OK Status
    """
    return jsonify({
        'status': 'OK'
    })


@app_views.route('/stats')
def clsCount():
    """
    Retrieve the number of each objects by type
    """
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
