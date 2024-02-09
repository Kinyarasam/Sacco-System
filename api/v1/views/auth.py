#!/usr/bin/env python3
# -*- coding utf-8 -*-
""" Objects that handle all default RestFul API actions for authentications
"""
from models.user_session import UserSession
from api.v1.views import auth_views
from flasgger.utils import swag_from
from flask import request, make_response, jsonify, abort
from models import storage
from models.user import User
import json


@auth_views.route('/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/auth/index.yml')
def handle_auth():
    """ Register a new user.
    """
    return make_response(jsonify({"status": "OK"}), 200)


@auth_views.route('/login', methods=['POST'], strict_slashes=False)
@swag_from('documentation/auth/login.yml')
def handle_login():
    """ Authenticate a user.
    """
    if "application/json" not in request.content_type:
        abort(400, description="Missing required parameters")

    userData = request.json

    if "email" not in userData.keys():
        abort(400, description="Missing required parameters <email>")

    if "password" not in userData.keys():
        abort(400, description="Missing required parameters <password>")

    user = User.find(**userData)
    
    if user is None:
        abort(401, description="Unauthorized")

    return make_response(jsonify({"data": user.to_dict()}), 200)

@auth_views.route('/register', methods=['POST'], strict_slashes=False)
@swag_from('documentation/auth/register.yml')
def handle_register():
    """ Register a new user.
    """
    if "application/json" not in request.content_type:
        abort(400, description="Missing required parameters")

    userData = request.json

    if 'email' not in userData.keys():
        abort(400, description="Missing required parameter <email>")

    if 'password' not in userData.keys():
        abort(400, description="Missing required parameter <password>")

    user = User(**userData)
    user.save()

    # generate a token
    session = UserSession(user_id=user.id)
    session.save()

    return make_response(jsonify({"token": session.id}), 201)
