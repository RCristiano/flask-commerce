from app import db
from app.user import User
from app.product import Product


class Cart(db.Model):
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Cart('{self.user_id}', '{self.product_id}, '{self.quantity}')"
