from flask import Blueprint

index_blu = Blueprint('index', __name__)
user_blu = Blueprint('user', __name__)

from . import index, user
