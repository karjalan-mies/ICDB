from webapp.db import db

class InsurancePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String)
    number = db.Column(db.Integer)
    date_of_issue = db.Column(db.Date)

    def __repr__(self):
        return f'<Policy {self.id} {self.series} {self.number}>'
