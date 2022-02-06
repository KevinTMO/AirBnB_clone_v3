from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


# Import class objects from models/storage

from models import storage
from models.state import State

# Import all files for handling RESTFul API actions of classes

from api.v1.views.index import *
from api.v1.views.states import *
