from flask import request, jsonify
from flask_login import login_user, login_required, logout_user
from app import db
from app.cart import cart
from app.cart.model import Cart


@cart.route('/')
def get_all():
    carts = Cart.query.all()
    return jsonify(str(carts))
