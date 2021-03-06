from app import login_manager
from app.user.model import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
