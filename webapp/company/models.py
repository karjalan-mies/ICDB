from webapp.db import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    inn = db.Column(db.String)
    address = db.Column(db.String)
    director = db.Column(db.String)

    def __repr__(self):
        return f'Организация {self.id} {self.name}'
