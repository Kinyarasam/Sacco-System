#!/usr/bin/env python3
# -*- coding utf-8 -*-
""" Objects that handle all default RestFul API actions for authentications
"""
from models.user_session import UserSession
from api.v1.views import auth_views
from flasgger.utils import swag_from
from flask import request, make_response, jsonify, abort


@auth_views.route('/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/auth/index.yml')
def handle_auth():
    """ Register a new user.
    """
    return make_response(jsonify({"status": "OK"}))


@auth_views.route('/register', methods=['POST'], strict_slashes=False)
@swag_from('documentation/auth/register.yml')
def handle_register():
    """ Register a new user.
    """
    # if 'Content-Type: application/json' not in request.headers:
    #     abort(400, description="Missing required parameters")

    # if not request.json:
    #     abort(400, description="Missing required parameters")

    userInfo = request.json

    if 'email' not in userInfo:
        abort(400, description="Missing required parameter: email")

    if 'password' not in userInfo:
        abort(400, description="Missing required parameter: email")

    return make_response(jsonify({"status": "OK"}))
