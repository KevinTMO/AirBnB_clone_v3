#!/usr/bin/python3
"""
Module: states.py

Handles all default RESTFul API actions:

"""

from flask import Flask, jsonify, abort, request, make_response
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def allObjs():
    """
    Get all objs from State
    """
    result = [objs.to_dict() for objs in storage.all('State').values()]
    return jsonify(result)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def getId(state_id):
    """
    Get the id of the states
    """
    st = storage.get('State', state_id)

    if st is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delState(state_id):
    """
    delete a state obj given by state_id
    """
    st = storage.get('State', state_id)

    if st is None:
        abort(404)
    st.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def createState():
    """
    Create a new State object
    """
    if not request.get_json():
        return jsonify({
            'error': 'Not a JSON'
        }), 400

    elif 'name' not in request.get_json():
        return jsonify({
            'error:' 'Missing name',
            400
        })
    else:
        objData = request.get_json()
        obj = State(**objData)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/states/<states_id>', methods=['PUT'], strict_slashes=False)
def updateState(state_id):
    """
    Update an existing state object
    """
    if not request.get_json():
        return jsonify({
            'error': 'Not a JSON',
        }), 400
    obj = storage.get('State', states_id)
    if obj is None:
        abort(404)
    objData = request.get_json()
    objName = objData['name']
    obj.save()
    return jsonify(obj.to_dict()), 200
