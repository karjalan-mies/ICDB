from datetime import timedelta

SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@127.0.0.1:5432/ICDB'

SECRET_KEY = 'kfkbyfbkjyfybccfyfkvthf'

REMEMBER_COOKIE_DURATION = timedelta(days=5)
SQLALCHEMY_TRACK_MODIFICATIONS = False