from flask import Blueprint
from app.cart.model import Cart

cart = Blueprint('cart', __name__)

from app.cart import handler
