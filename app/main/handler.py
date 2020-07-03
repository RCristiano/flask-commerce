from flask_login import login_required
from app.main import main

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return 'Ok'
