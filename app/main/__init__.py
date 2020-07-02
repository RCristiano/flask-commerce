from flask import Blueprint
from flask_login import login_required
from app import db, auth
from app.user import User

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return 'Ok'
