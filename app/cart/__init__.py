from app import db


class Cart(db.Model):
    __table_args__ = {'extend_existing': True}
    userid = db.Column(db.Integer, db.ForeignKey(
        'user.userid'), nullable=False, primary_key=True)
    productid = db.Column(db.Integer, db.ForeignKey(
        'product.productid'), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Cart('{self.userid}', '{self.productid}, '{self.quantity}')"
