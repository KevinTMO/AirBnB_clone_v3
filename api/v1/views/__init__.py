from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


# Import class objects from models/storage

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User

# Import all files for handling RESTFul API actions of classes

from api.v1.views.index import *
from api.v1.views.states import *
# from api.v1.views.cities import *
# from api.v1.views.amenities import *
# from api.v1.views.users import *
# from api.v1.views.places import *
# from api.v1.views.reviews import *
