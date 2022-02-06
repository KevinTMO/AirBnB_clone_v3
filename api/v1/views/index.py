#!/usr/bin/python3
"""
Module: index.py

Configuring a route to return JSON string
"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """
    return a JSON string: OK Status
    """
    return jsonify({
        'status': 'OK'
    })
