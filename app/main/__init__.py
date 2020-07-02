from flask import Blueprint
from flask_login import login_required
from app import db, auth

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return 'Ok'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    user = User.query.filter_by(email=form.email.data.lower()).first()
    if user is not None and user.verify_password(form.password.data):
        login_user(user)
        next = request.args.get('next')
        if next is None or not next.startswith('/'):
            next = url_for('main.index')
        return redirect(next)
    flash('Invalid email or password.')
    return 'User has not access'
