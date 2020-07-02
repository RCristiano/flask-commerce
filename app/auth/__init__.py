from app.user import User
from flask import Blueprint, request, jsonify, url_for, redirect, flash
from flask_login import login_user
import json

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user is not None and user.verify_password(request.form.get('password')):
        login_user(user, request.form.get('remenber_me'))
        return 'Access granted'
    x = User.query.all()
    return jsonify(x[0])
    # return 'User has not access'
