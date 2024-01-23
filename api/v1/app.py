#!/usr/bin/python3
""" Flask Application """
# from flask_cors import CORS
from models import storage
from flask import Flask, make_response, jsonify, abort, request
from api.v1.views import app_views
from api.v1.views import auth_views
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.register_blueprint(auth_views)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

auth = None
AUTH_TYPE = ''  # Get the user auth level
if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request():
    """Filter each request before it's handled by the proper route
    """
    if auth is not None:
        setattr(request, "current_user", auth.current_user(request))
        excluded = [
            'api/v1/status/',
            'api/v1/unauthorized/',
            'api/v1/forbidden/',
            'api/v1/auth_session/*',
        ]
        if auth.require_auth(request.path, excluded):
            cookie = auth.session_cookie(request)
            if auth.authorization_header(request) is None and cookie is None:
                abort(401, description="Unauthorized")
            if auth.current_user(request) is None:
                abort(403, description="Forbidden")


@app.teardown_appcontext
def close_db(error):
    """ Close Storage
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
        404:
            description: a resource was not found
    """
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(401)
def unauthorized(error):
    """ 401 Error
    ---
    responses:
        401:
            description: Not allowed to access a resource
    """
    return make_response(jsonify({"error": "Unauthorized"}), 401)


@app.errorhandler(400)
def missing(error):
    """ 400 Error
    ---
    responses:
        400:
            description: a parameter was not found
    """
    return make_response(jsonify({"error": "{}".format(error)}), 400)


app.config['SWAGGER'] = {
    'title': 'Sacco System Restful API',
    'uiversion': 3
}

Swagger(app)
