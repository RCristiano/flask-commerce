from flask import request, jsonify
from flask_login import login_required
from app import db
from app.product import product
from app.product.model import Product


def product_as_dict(product):
    return {"product_id": product.id,
            "product_name": product.product_name,
            "description": product.description,
            "image": product.image,
            "price": str(product.regular_price),
            "discounted": str(product.discounted_price),
            "in_stock": product.quantity}


@product.route('/')
@login_required
def get_all():
    products = Product.query.all()
    return jsonify([product_as_dict(product) for product in products])


@product.route('/<int:id>', methods=['GET'])
@login_required
def get_by(id: int):
    product = Product.query.filter_by(id=id).first()
    if product is not None:
        return jsonify(product_as_dict(product))
    return jsonify(msg='Product not found'), 404

@product.route('/register', methods=['POST'])
@login_required
def register():
    product = Product(product_name=request.form.get('product_name'),
                      description=request.form.get('description'),
                      image=request.form.get('image'),
                      quantity=request.form.get('quantity'),
                      regular_price=request.form.get('regular_price'),
                      discounted_price=request.form.get('discounted_price'))
    db.session.add(product)
    db.session.commit()
    return jsonify(product_as_dict(product))


@product.route('/update/<int:id>', methods=['PUT', 'PATCH'])
@login_required
def update(id: int):
    product = Product.query.filter_by(id=id).first()
    if product == None:
        return jsonify(msg='Product not found'), 404
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
    return jsonify(product_as_dict(product))


@product.route('/remove', methods=['DELETE'])
@login_required
def remove():
    product = Product.query.filter_by(id=request.form.get('id')).first()
    if product == None:
        return jsonify(msg='Product not found'), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify(msg='Product has been removed')
