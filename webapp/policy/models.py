from webapp.db import db

class TypeOfPolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)


class InsurancePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String)
    number = db.Column(db.Integer)
    date_of_issue = db.Column(db.Date)
    type = db.Column(db.Integer, db.ForeignKey(TypeOfPolicy.id), index=True, nullable=False)
    company = db.Column(db.Integer, db.ForeignKey(db.Company.id), index=True, nullable=False)

    def __repr__(self):
        return f'<Policy {self.id} {self.series} {self.number}>'
