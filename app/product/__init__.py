from app import db


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
        return f"Product('{self.productid}','{self.product_name}'," \
               f"'{self.description}', '{self.image}', '{self.quantity}'," \
               f"'{self.regular_price}', '{self.discounted_price}')"
