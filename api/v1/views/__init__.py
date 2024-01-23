#!/usr/bin/env python3
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.users import *

auth_views = Blueprint('auth_views', __name__, url_prefix='/api/v1/auth_session')
from api.v1.views.auth import *
