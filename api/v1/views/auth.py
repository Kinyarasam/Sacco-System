#!/usr/bin/env python3
# -*- coding utf-8 -*-
""" Objects that handle all default RestFul API actions for authentications
"""
from models.user_session import UserSession
from api.v1.views import auth_views
from flasgger.utils import swag_from
from flask import request, make_response, jsonify, abort, redirect, render_template, url_for
from models import storage
from models.user import User
from models.utils.redis_client import redisClient


@auth_views.route('/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/auth/index.yml')
def handle_auth():
    """ redirect to the login url
    """
    return redirect('{}/login'.format(request.path))


@auth_views.route('/login', methods=['GET'], strict_slashes=False)
def render_login():
    """login page view
    """
    return render_template('login.html')


@auth_views.route('/login', methods=['POST'], strict_slashes=False)
@swag_from('documentation/auth/login.yml')
def handle_login():
    """ Authenticate a user.
    """
    if "application/json" not in request.content_type:
        abort(400, description="Missing required parameters")

    userData = request.get_json()

    if "email" not in userData.keys():
        abort(400, description="Missing required parameters <email>")

    if "password" not in userData.keys():
        abort(400, description="Missing required parameters <password>")

    user = User.find(**userData)

    if user is None:
        abort(401, description="Unauthorized")

    # generate a token
    session = UserSession(user_id=user.id)

    key = 'auth_{}'.format(session.id)
    redisClient.set(key, user.id, 60)

    return make_response(jsonify({"token": session.id}), 200)


@auth_views.route('/register', methods=['POST'], strict_slashes=False)
@swag_from('documentation/auth/register.yml')
def handle_register():
    """ Register a new user.
    """
    if "application/json" not in request.content_type:
        abort(400, description="Missing required parameters")

    userData = request.get_json()

    if 'email' not in userData.keys():
        abort(400, description="Missing required parameter <email>")

    if 'password' not in userData.keys():
        abort(400, description="Missing required parameter <password>")

    user = User.find(**userData)
    if user is not None:
        abort(400, description="User already exists")

    user = User(**userData)
    user.save()

    return make_response(jsonify({"user": user.to_dict()}), 201)

# @auth_views.route('/static/styles', methods=['GET'], strict_slashes=False)
# def get_css():
#     """Make the css styling available
#     """
#     from os import getcwd, listdir
#     current_dir = getcwd()
#     static_dir = '{}/api/v1/templates/static/styles'.format(str(getcwd()))
#     files = ['{}/{}'.format(static_dir, file)
#              for file in listdir(static_dir) if str(file).endswith('.css')]

#     data = ''
#     for file in files:
#         with open(file, mode='r', encoding='utf8') as f:
#             data += str(f.read())
#             data += '\n'

#     return data
