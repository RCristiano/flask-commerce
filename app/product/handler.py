from flask import request, jsonify
from flask_login import login_required
from sqlalchemy.exc import IntegrityError
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
    """List product by id
    List a product with the requested `id`
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
            description: Product model
            properties:
                product_id:
                    name: product_id
                    type: integer
                product_name:
                    in: formData
                    name: product_name
                    type: string
                    required: true
                description:
                    in: formData
                    name: description 
                    type: string
                    required: true
                image:
                    in: formData
                    name: image 
                    type: string
                    required: true
                in_storage:
                    in: formData
                    name: quantity
                    type: integer
                    required: true
                regular_price:
                    in: formData
                    name: regular_price 
                    type: string
                    format: double
                discounted_price:
                    in: formData
                    name: discounted_price 
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
    """Register a product
    Register and show the registered product
    ---
    security:
        - cookieAuth: []
    tags:
        - Product
    produces:
        - application/json
    parameters:
        - $ref: '#/definitions/Product/properties/product_name'
        - $ref: '#/definitions/Product/properties/description'
        - $ref: '#/definitions/Product/properties/image'
        - $ref: '#/definitions/Product/properties/in_storage'
        - $ref: '#/definitions/Product/properties/regular_price'
        - $ref: '#/definitions/Product/properties/discounted_price'
    responses:
        200:
            description: Return registered product.
            schema:
                type: array
                items:
                    $ref: '#/definitions/Product'
        400:
            description: Message for when parameters are wrong or missing.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Invalid fields or missing fields
        401:
            $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    try:
        product = Product(product_name=request.form.get('product_name'),
                        description=request.form.get('description'),
                        image=request.form.get('image'),
                        quantity=request.form.get('quantity'),
                        regular_price=request.form.get('regular_price'),
                        discounted_price=request.form.get('discounted_price'))
        db.session.add(product)
        db.session.commit()
        return jsonify(product_as_dict(product))
    except (IntegrityError, TypeError, AttributeError):
        return jsonify(msg='Invalid fields or missing fields'), 400


@product.route('/update/<int:id>', methods=['PUT', 'PATCH'])
@login_required
def update(id: int):
    """Update a product
    Update and show the updated product
    Only the parameters entered will be changed
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
        - required: false
          allOf:
          - $ref: '#/definitions/Product/properties/product_name'
        - required: false
          allOf:
          - $ref: '#/definitions/Product/properties/description'
        - required: false
          allOf:
          - $ref: '#/definitions/Product/properties/image'
        - required: false
          allOf:
          - $ref: '#/definitions/Product/properties/in_storage'
        - $ref: '#/definitions/Product/properties/regular_price'
        - $ref: '#/definitions/Product/properties/discounted_price'
    responses:
        200:
            description: Return updated product.
            schema:
                type: array
                items:
                    $ref: '#/definitions/Product'
        401:
            $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    product = Product.query.filter_by(id=id).first()
    if product is None:
        return jsonify(msg='Product not found'), 404
    try:
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
    except (IntegrityError, TypeError, AttributeError):
        return jsonify(msg='Invalid fields or missing fields'), 400


@product.route('/remove', methods=['DELETE'])
@login_required
def remove():
    """Removes a product
    Removes a product with the requested `id`
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
        in: formData
        type: integer
        required: true
        example: 1
    responses:
        200:
            description: Confirms removal.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Product has been removed
        200:
            description: Product not found with request `id`.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Product not found
        401:
            $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    product = Product.query.filter_by(id=request.form.get('id')).first()
    if product is None:
        return jsonify(msg='Product not found'), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify(msg='Product has been removed')
