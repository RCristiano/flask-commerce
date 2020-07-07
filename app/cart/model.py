from app import db
from app.product import Product


def item_as_dict(item):
    product = Product.query.filter_by(id=item.product_id).first()
    return {"item_id": item.product_id,
            "product_name": product.product_name,
            "image": product.image,
            "price": str(product.regular_price),
            "discounted": str(product.discounted_price),
            "quantity": item.quantity}


class Cart(db.Model):
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"item('{self.user_id}', '{self.product_id}, '{self.quantity}')"
