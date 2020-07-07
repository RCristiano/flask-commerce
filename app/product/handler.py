from flask import request, jsonify
from flask_login import login_required
from app import db
from app.product import product
from app.product.model import Product, product_as_dict


@product.route('/')
@login_required
def get_all():
    """List products
    List all products in store
    ---
    security:
        - cookieAuth: []
    tags:
        - Product
    produces:
        - application/json
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
    products = Product.query.all()
    return jsonify([product_as_dict(product) for product in products])


@product.route('/<int:id>', methods=['GET'])
@login_required
def get_by(id: int):
    """List products
    List all products in storage
    ---
    security:
        - cookieAuth: []
    tags:
        - Product
    produces:
        - application/json
    parameters:
      - id: id
        name: id
        in: path
        type: integer
        required: true
        example: 1
    definitions:
        Product:
            type: object
            description: describe
            properties:
                product_id:
                    type: integer
                product_name:
                    type: string
                description:
                    type: string
                image:
                    type: string
                in_storage:
                    type: integer
                regular_price:
                    type: string
                    format: double
                discounted_price:
                    type: string
                    format: double
    responses:
        200:
            description: List of all products.
            schema:
                $ref: '#/definitions/Product'
        401:
            $ref: '#/definitions/Unauthorized'
        404:
            description: Product not found
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Product not found
        default:
            description: Unexpected error.
    """
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
