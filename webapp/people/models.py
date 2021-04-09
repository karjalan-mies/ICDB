from webapp.db import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    patronymic = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    birth_date = db.Column(db.Date)

    def __repr__(self):
        return f'People {self.id} {self.last_name} {self.first_name} {self.patronymic} {self.birth_date}'