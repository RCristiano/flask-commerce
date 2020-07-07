from app import db


def product_as_dict(product):
    return {"product_id": product.id,
            "product_name": product.product_name,
            "description": product.description,
            "image": product.image,
            "price": format(product.regular_price, '.2f'),
            "discounted": format(product.discounted_price, '.2f'),
            "in_storage": product.quantity}


class Product(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    regular_price = db.Column(db.DECIMAL)
    discounted_price = db.Column(db.DECIMAL)

    def __repr__(self):
        return f"Product('{self.id}','{self.product_name}'," \
               f"'{self.description}', '{self.image}', '{self.quantity}'," \
               f"'{self.regular_price}', '{self.discounted_price}')"
