from app.user import User
from flask import Blueprint, request, jsonify, url_for, redirect, flash
from flask_login import login_user
import json

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():

    user = User.query.filter_by(email=request.form.get('email').lower()).first()
    if user is not None and user.verify_password(request.form.get('password')):
        login_user(user)
        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('main.index')
        return redirect(next)
    flash('Invalid email or password.')
    return 'User has not access'
