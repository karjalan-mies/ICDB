from webapp.db import db

class InsuranceEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_event = db.Column(db.Date)
    type_event = db.Column(db.String(100))
