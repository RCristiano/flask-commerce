from math import exp
from flask import request, jsonify
from flask_login import login_required, current_user
from app import db
from app.cart import cart
from app.cart.model import Cart, item_as_dict
from app.user.model import User
from app.product.model import Product


@cart.route('/user_cart')
@login_required
def get_by_user(id: int = False):
    """Show cart
    Show cart by logged user's `id`
    Gets the user's `id` from the session
    Cart is a list of products in the user's cart
    The cart can be an empty list
    ---
    security:
        - cookieAuth: []
    tags:
        - Cart
    produces:
        - application/json
    responses:
        200:
            description: Show user cart.
            schema:
                type: array
                items:
                    $ref: '#/definitions/Product'
        401:
            $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    user_id = id if id else User.get_id(current_user)
    cart = Cart.query.filter_by(user_id=user_id).all()
    return jsonify([item_as_dict(item) for item in cart])


@cart.route('/manage_cart', methods=['POST', 'PUT', 'PATCH'])
@login_required
def manage_cart():
    """Manage cart
    Manage the cart
    Add a product: Insert a product in the cart with `product id` and `quantity`
    Update quantity in cart: Edit `quantity` of a product by `product id`
    Remove product: Set quantity to zero of a product by `product id`
    ---
    security:
        - cookieAuth: []
    tags:
        - Cart
    produces:
        - application/json
    parameters:
        - in: formData
          name: product_id
          type: integer
          required: true
        - in: formData
          name: quantity
          type: integer
          required: true
    responses:
        200:
            description: List of all products.
            schema:
                type: array
                items:
                    $ref: '#/definitions/Product'
        401:
            $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    user_id = User.get_id(current_user)
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
    except ValueError:
        return jsonify(msg='Invalid fields or missing fields'), 400

    try:
        storage = int(Product.query.filter_by(id=product_id).first().quantity)
    except AttributeError:
        return jsonify(msg='Product not found'), 404

    if not storage:
        return jsonify(msg='Out of storage'), 400
    item = Cart.query.filter_by(user_id=user_id,
                                product_id=product_id).first()
    if item:
        if not quantity:
            db.session.delete(item)
            db.session.commit()
            return jsonify(msg='Item has been removed')
        item.quantity = quantity
    else:
        if not quantity:
            return jsonify(msg='Quantity invalid'), 400
        item = Cart(user_id=user_id,
                    product_id=product_id,
                    quantity=quantity)
    if quantity > storage:
        return jsonify(msg='This quantity is not in store'), 400
    db.session.add(item)
    db.session.commit()
    cart = Cart.query.filter_by(user_id=user_id).all()
    return jsonify([item_as_dict(item) for item in cart])
