#!/usr/bin/python3
""" Flask Application """
# from flask_cors import CORS
from models import storage
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


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
