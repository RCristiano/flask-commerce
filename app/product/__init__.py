from flask import Blueprint
from app.product.model import Product

product = Blueprint('product', __name__)

from app.product import handler
