from webapp.db import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100))


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(100))


class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_number = db.Column(db.String(10))
    VIN = db.Column(db.String(17))
    brand = db.Column(db.Integer, db.ForeignKey(Brand.id), index=True, nullable=False)
    model = db.Column(db.Integer, db.ForeignKey(Model.id), index=True, nullable=False)
    color = db.Column(db.Integer, db.ForeignKey(Color.id), index=True, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey(People.id), index=True, nullable=False)
    policy = db.Column(db.Integer, db.ForeignKey(InsurancePolicy.id), index=True, nullable=False)

    def __repr__(self):
        return f'Транспортное средство {self.id} {self.brand} {self.model} {self.reg_number}'
