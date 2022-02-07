#!/usr/bin/python3
"""
Module: states.py

Handles all default RESTFul API actions:

"""

from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def allObjs():
    """
    Get all objs from State
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
            }), 400
        obj = State(objData.get('name'))
        obj.save()
        return jsonify(obj.to_dict()), 201

    # IF NOT POST THEN GET BELOW

    state = storage.all('State')
    result = [objs.to_dict() for objs in storage.all('State').values()]
    return jsonify(result)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def getId(state_id):
    """
    Get the id of the states
    """
    st = storage.get('State', state_id)

    if st is None:
        abort(404)

    if request.method == 'DELETE':
        storage.delete(st)
        # st.delete()
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':

        objData = request.get_json()

        if not objData:
            return jsonify({
                'error': 'Not a JSON'
            }), 400

        objData['id'] = st.id
        objData['created_at'] = st.created_at
        st.__init__(**objData)
        st.save()
        return jsonify(st.to_dict()), 200

    return jsonify(st.to_dict())
