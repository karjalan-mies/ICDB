from webapp.db import db

class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(7))


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    patronymic = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    birth_date = db.Column(db.Date)
    gender_id = db.Column(db.Integer, db.ForeignKey(Gender.id), index=True, nullable=True)
#    addresses = relationship('PeoplesAndAddresses', back_populates='address', lazy='joined')

    def __repr__(self):
        return f'People {self.id} {self.last_name} {self.first_name} {self.patronymic} {self.birth_date}'