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
    return jsonify(st.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delState(state_id):
    """
    delete a state obj given by state_id
    """
    if request.method == 'DELETE':
        st = storage.get('State', state_id)
        if st is None:
            abort(404)
        storage.delete(st)
        # st.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def createState():
    """
    Create a new State object
    """
    if request.method == 'POST':
        objData = request.get_json()
        if not objData:
            return jsonify({
                'error': 'Not a JSON'
            }), 400

        elif 'name' not in objData:
            return jsonify({
                'error:' 'Missing name',
                400
            })
        obj = State(**objData)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def updateState(state_id):
    """
    Update an existing state object
    """
    if request.method == 'PUT':

        objData = request.get_json()

        if not objData:
            return jsonify({
                'error': 'Not a JSON'
            }), 400

        obj = storage.get('State', state_id)

        if obj is None:
            abort(404)

        objData['id'] = obj.id
        objData['created_at'] = obj.created_at
        objSt.__init__(**objData)
        objSt.save()
        return jsonify(objSt.to_dict()), 200
