from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thumb = db.Column(db.String(50))
    name = db.Column(db.String(30))
    price = db.Column(db.Float)
    description = db.Column(db.Text(300))
    box_x = db.Column(db.Float)
    box_y = db.Column(db.Float)
    font_path = db.Column(db.String(50))
    font_size = db.Column(db.Integer)
    font_color_r = db.Column(db.Integer)
    font_color_g = db.Column(db.Integer)
    font_color_b = db.Column(db.Integer)

    def __repr__(self):
        return '<Name = {}>'.format(self.name)
