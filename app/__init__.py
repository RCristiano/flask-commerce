from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.access_denied'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    from app.main import main as main_blueprint
    from app.auth import auth as auth_blueprint
    from app.product import product as product_blueprint
    from app.cart import cart as cart_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(cart_blueprint, url_prefix='/carts')

    return app
