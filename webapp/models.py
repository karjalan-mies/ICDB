from flask_login import UserMixin
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# Отношения к Адресу
class RelationPeopleAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_relation = db.Column(db.String(100))


class RelationCompanyAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_relation = db.Column(db.String(100))


# class PeoplesAndAddresses(db.Model):
#     people_id = db.Column(db.Integer, db.ForeignKey('peoples.id'), primary_key=True)
#     address_id = db.Column(db.Integer, db.ForeignKey('address.id'), primary_key=True)
#
#     type_relation = db.Column(db.Integer, db.ForeignKey(RelationPeopleAddress.id), index=True, nullable=False)
#
#     peoples = relationship('People', back_populates='address')
#     address = relationship('Address', back_populates='peoples')


class CompaniesAndAddresses(db.Model):
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), primary_key=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), primary_key=True)

    # relation_type = db.Column(db.Integer, db.ForeignKey(RelationCompanyAddress.id), index=True, nullable=False)
    #
    # peoples = relationship('People', back_populates='address', lazy='joined')
    # address = relationship('Address', back_populates='peoples', lazy='joined')


# Сущность Физическое лицо
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


# Сущность Адрес
class FullAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
#    full_address = db.Column(Integer, ForeignKey(FullAddress.id), index=True, nullable=False)
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    house_number = db.Column(db.Integer)
    building = db.Column(db.String(5))
    possession = db.Column(db.String(5))
    apartment = db.Column(db.Integer)
    # peoples = relationship('PeoplesAndAddresses', back_populates='peoples', lazy='joined' ,)
    # company = relationship('CompaniesAndAddresses', back_populates='company', lazy='joined' ,)

    def __repr__(self):
        return f'Адрес {self.id} {self.full_address}'


# Сущность Страховой полис
class TypeOfPolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)


# Сущность Компания
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def __repr__(self):
        return f'Организация {self.id} {self.name}'


class InsurancePolicy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.String)
    number = db.Column(db.Integer)
    date_of_issue = db.Column(db.Date)
    type = db.Column(db.Integer, db.ForeignKey(TypeOfPolicy.id), index=True, nullable=False)
    company = db.Column(db.Integer, db.ForeignKey(Company.id), index=True, nullable=False)

    def __repr__(self):
        return f'<Policy {self.id} {self.series} {self.number}>'


# Сущность Транспортное средство
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


# Сущность Страховой случай
class InsuranceEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_event = db.Column(db.Date)
    type_event = db.Column(db.String(100))
    participants = db.Column(db.Integer, db.ForeignKey(People.id), index=True, nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10))

    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    @property
    def is_admin(self):
        return self.role == 'admin'


    def __repr__(self):
        return f'<User {self.username}>'
