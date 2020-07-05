from flask import request, jsonify
from flask_login import login_required, current_user
from app import db
from app.cart import cart
from app.cart.model import Cart
from app.user.model import User
from app.product.model import Product


@cart.route('/user_cart')
@login_required
def get_by_user(id: int = False):
    user_id = id if id else User.get_id(current_user)
    cart = Cart.query.filter_by(user_id=user_id).all()
    return jsonify(str(cart))


@cart.route('/manage_cart', methods=['POST'])
@login_required
def manage_cart():
    user_id = User.get_id(current_user)
    product_id= request.form.get('product_id')
    quantity = int(request.form.get('quantity'))
    stock = int(Product.query.filter_by(id=product_id).first().quantity)
    if not stock:
        return jsonify({'msg': 'Out of stock'}), 400
    item = Cart.query.filter_by(user_id=user_id,
                                product_id=product_id).first()
    if item:
        if not quantity:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'msg': 'Item has been removed'})
        item.quantity = quantity
    else:
        if not quantity:
            return jsonify({'msg': 'Quantity invalid'}), 400
        item = Cart(user_id=user_id,
                    product_id=product_id,
                    quantity=quantity)
    if quantity > stock:
        return jsonify({'msg': 'Out of stock for this quantity'}), 400
    db.session.add(item)
    db.session.commit()
    cart = Cart.query.filter_by(user_id=user_id).all()
    return jsonify(str(cart))
