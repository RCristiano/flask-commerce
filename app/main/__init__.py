from flask import Blueprint
from flask_login import login_required
from app import db, auth
from app.user import User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return 'Ok'
