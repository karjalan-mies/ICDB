from webapp.db import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    house_number = db.Column(db.Integer)
    building = db.Column(db.String(5))
    possession = db.Column(db.String(5))
    apartment = db.Column(db.Integer)

    def __repr__(self):
        return f'Адрес {self.id}'
