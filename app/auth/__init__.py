from app import db
from app.user import User
from flask import Blueprint, request, jsonify
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user is not None and user.verify_password(request.form.get('password')):
        login_user(user, request.form.get('remember_me'))
        return 'Access granted'
    return 'User has not access'


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'User has been logged out'


@auth.route('/access_denied')
def access_denied():
    return 'Access denied'


@auth.route('/register', methods=['POST'])
def register():
    user = User(name=request.form.get('name'),
                password=request.form.get('password'),
                address=request.form.get('address'),
                email=request.form.get('email').lower(),
                phone=request.form.get('phone'))
    db.session.add(user)
    db.session.commit()
    return jsonify(str(user.id))
