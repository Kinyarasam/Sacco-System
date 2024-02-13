#!/usr/bin/env python3
"""Objects that handle all default RestFul API actions for Users
"""


from models.user import User
from models.utils.redis_client import redisClient
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


def get_authenticated_user():
    token = request.headers.get("Authorization")
    if token is None:
        abort(401, description="Unauthorized")

    key = 'auth_{}'.format(token)
    user_id = redisClient.get(key)
    if user_id is None:
        abort(401, description="Unauthorized")

    user = User.find(id=user_id)
    if user is None:
        abort(401, description="Unauthorized")

    return user


@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/me.yml')
def is_authenticated():
    """Retrieve the currently authenticated user.
    """
    user = get_authenticated_user()
    return make_response(jsonify(user.to_dict()), 200)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_users():
    """Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    list_users = []
    [list_users.append(user.to_dict()) for user in all_users]
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml')
def get_one_user(user_id=None):
    """Retrieve a specific user based on id
    """
    if user_id is None:
        abort(404, description="User {:s} not found".format(user_id))

    user = storage.get(User, id=user_id)
    if not user:
        abort(404)

    return make_response(jsonify(user.to_dict()), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml')
def post_user():
    """Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    user = User.find(**data)
    if user is not None:
        abort(400, description="User already exists")

    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/user/delete_user.yml')
def delete_user(user_id=None):
    """Deletes a user object
    """
    if user_id is None:
        abort(404)

    user = storage.get(User, id=user_id)
    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)
