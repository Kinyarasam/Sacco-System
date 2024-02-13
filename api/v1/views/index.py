#!/usr/bin/env python3
""" Index """

from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each object by type
    """
    classes = [User]
    names = ['users']

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)


@app_views.route('/static/styles', methods=['GET'], strict_slashes=False)
def get_css():
    """Make the css styling available
    """
    from os import getcwd, listdir
    current_dir = getcwd()
    static_dir = '{}/api/v1/templates/static/styles'.format(str(getcwd()))
    files = ['{}/{}'.format(static_dir, file)
             for file in listdir(static_dir) if str(file).endswith('.css')]

    data = ''
    for file in files:
        with open(file, mode='r', encoding='utf8') as f:
            data += str(f.read())
            data += '\n'

    return data
    # with open()
