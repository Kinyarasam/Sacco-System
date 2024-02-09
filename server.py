#!/usr/bin/env python3
"""Flask app server
"""

from os import environ
from api.v1.app import app


if __name__ == "__main__":
    """ Main Function
    """
    host = environ.get('SACCO_API_HOST')
    port = environ.get('SACCO_API_PORT')

    host = '0.0.0.0' if not host else host
    port = '5000' if not port else port
    app.run(host=host, port=port, threaded=True)
