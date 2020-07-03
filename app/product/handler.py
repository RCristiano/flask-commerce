from flask import request, jsonify
from flask_login import login_user, login_required, logout_user
from app import db
from app.product import product
from app.product.model import Product


@product.route('/')
def get_all():
    products = Product.query.all()
    return jsonify(str(products))


@product.route('/<int:id>', methods=['GET'])
def get_by(id: int):
    product = Product.query.filter_by(id=id).first()
    if product is not None:
        return jsonify(str(product))
    return jsonify('Product not found'), 404

@product.route('/register', methods=['POST'])
def register():
    product = Product(product_name=request.form.get('product_name'),
                      description=request.form.get('description'),
                      image=request.form.get('image'),
                      quantity=request.form.get('quantity'),
                      regular_price=request.form.get('regular_price'),
                      discounted_price=request.form.get('discounted_price'))
    db.session.add(product)
    db.session.commit()
    return jsonify(str(product.id))


@product.route('/update/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    product = Product.query.filter_by(id=id).first()
    if product == None:
        return jsonify('Product not found'), 404
    product.product_name = request.form.get('product_name') \
        or product.product_name
    product.description = request.form.get('description') \
        or product.description
    product.image = request.form.get('image') \
        or product.image
    product.quantity = request.form.get('quantity') \
        or product.quantity
    product.regular_price = request.form.get('regular_price') \
        or product.regular_price
    product.discounted_price = request.form.get('discounted_price') \
        or product.discounted_price
    db.session.add(product)
    db.session.commit()
    return jsonify(str(product))


@product.route('/remove', methods=['DELETE'])
def remove():
    product = Product.query.filter_by(id=request.form.get('id')).first()
    if product == None:
        return jsonify('Product not found'), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify('Product has been removed')
