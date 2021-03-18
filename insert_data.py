from db import db_session
from models import Gender

for val in ['Мужской', 'Женский']:
    gender = Gender(gender=val)
    db_session.add(gender)
    db_session.commit()
