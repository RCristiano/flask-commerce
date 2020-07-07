from flask import request, jsonify
from flask import json
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from app import db
from app.auth import auth
from app.user import User


@auth.route('/login', methods=['POST'])
def login():
    """Login
    Authenticate the user with e-mail and password.
    ---
    tags:
        - Authentication
    consumes:
        - application/x-www-form-urlencoded
    produces:
        - application/json
    components:
        securitySchemes:
            cookieAuth:
                type: apiKey
                in: cookie
                name: session
    parameters:
        - $ref: "#/definitions/User/properties/Email"
        - $ref: "#/definitions/User/properties/Password"
    responses:
        200:
            description: Access granted message.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Access granted
            headers: 
                Set-Cookie:
                    schema: 
                        type: string
                        example: session=abcde12345; Path=/; HttpOnly
        400:
            description: Message for when parameters are wrong.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: "Invalid username/password supplied"
        default:
            description: Unexpected error.
    """
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user is not None and user.verify_password(request.form.get('password')):
        login_user(user, request.form.get('remember_me'))
        return jsonify(msg='Access granted')
    return jsonify(msg='Invalid username/password supplied'), 400


@auth.route('/logout')
@login_required
def logout():
    """Logout endpoint
    Endpoint to logout user from API session
    ---
    security:
        - cookieAuth: []
    tags:
        - Authentication
    produces:
        - application/json
    responses:
        200:
            description: Logout message.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: User has been logged out
        401:
            description:
                Unauthorized access because the user is not yet logged in.
            allOf:
            - $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    logout_user()
    return jsonify(msg='User has been logged out')


@auth.route('/access_denied')
def access_denied():
    """Access denied response
    Access denied endpoints receive a response from that endpoint
    ---
    tags:
        - Authentication
    produces:
        - application/json
    definitions:
        Unauthorized:
            description: Unauthorized access
            allOf:
            - $ref: '#/definitions/ApiResponse'
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Access denied
    responses:
        401:
            $ref: '#/definitions/Unauthorized'
        default:
            description: Unexpected error.
    """
    return jsonify(msg='Access denied'), 401


@auth.route('/register', methods=['POST'])
def register():
    """Register user
    Register a new user.
    ---
    tags:
        - Authentication
    consumes:
        - application/x-www-form-urlencoded
    produces:
        - application/json
    definitions:
        User:
            type: object
            description: User model
            properties:
                Email:
                    name: email
                    in: formData
                    type: string
                    required: true
                    example: email@email.com
                Password:
                    name: password
                    in: formData
                    type: string
                    required: true
                    example: password
                Name:
                    name: name
                    in: formData
                    type: string
                    required: true
                    example: Rodrigo
                Address:
                    name: address
                    in: formData
                    type: string
                    required: false
                    example: Street 1
                Phone:
                    name: phone
                    in: formData
                    type: string
                    required: false
                    example: 5555-5555
    parameters:
        - $ref: "#/definitions/User/properties/Name"
        - $ref: "#/definitions/User/properties/Email"
        - $ref: "#/definitions/User/properties/Password"
        - $ref: "#/definitions/User/properties/Address"
        - $ref: "#/definitions/User/properties/Phone"
    responses:
        200:
            description: User registred.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: User has been successfully registered
        400:
            description: Message for when parameters are wrong or missing.
            schema:
                allOf:
                - $ref: '#/definitions/ApiResponse'
                example:
                    msg: Invalid fields or missing fields
        default:
            description: Unexpected error.
    """
    try:
        user = User(name=request.form.get('name'),
                    password=request.form.get('password'),
                    address=request.form.get('address'),
                    email=request.form.get('email').lower(),
                    phone=request.form.get('phone'))
        db.session.add(user)
        db.session.commit()
        return jsonify(msg='User has been successfully registered'), 201
    except (IntegrityError, TypeError, AttributeError):
        return jsonify(msg='Invalid fields or missing fields'), 400
