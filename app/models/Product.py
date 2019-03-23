from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thumb = db.Column(db.String(50), index=True, unique=True)
    name = db.Column(db.String(30), index=True, unique=True)
    price = db.Column(db.Float, index=True, unique=True)
    description = db.Column(db.Text(300), index=True, unique=True)

    # def __init__(self, id, thumb, name, price, description):
    #     self.id = id
    #     self.thumb = thumb
    #     self.name = name
    #     self.price = price
    #     self.description = description

    def __repr__(self):
        return '<Name = {}>'.format(self.name)

# p = Product(thumb="dummy.jpeg", name="Caixa", price=4.90, description="Caixa para embalar presente")