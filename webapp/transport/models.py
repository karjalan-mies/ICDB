from webapp.db import db

class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_number = db.Column(db.String(10))
    VIN = db.Column(db.String(17))
    brand = db.Column(db.String)
    models_auto = db.Column(db.String)
    color = db.Column(db.String)
    owner = db.Column(db.String)

    def __repr__(self):
        return f'Транспортное средство {self.id} {self.brand} {self.models_auto} {self.reg_number}'
