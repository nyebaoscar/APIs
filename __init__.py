from flask import Blueprint

products = Blueprint('orders' , __name__, url_prefix='/api/v1/')

from . import views
