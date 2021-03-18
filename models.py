from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine


class TypeRelation(Base):
    __tablename__ = 'type_relation'
    id = Column(Integer, primary_key=True)
    type_relation = Column(String(100))


class RelationToAddress(Base):
    __tablename__ = 'relation_to_address'
    peoples_id = Column(Integer, ForeignKey('peoples.id'), primary_key=True)
    address_id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    organization_id = Column(Integer, ForeignKey('organization.id'), primary_key=True)
    relation_type = Column(Integer, ForeignKey(TypeRelation.id), index=True, nullable=False)

    peoples = relationship('People', backref='address_associations')
    peoples_address = relationship('Address', backref='peoples_associations')
    organizations_address = relationship('Address', backref='organizations_associations')
    organizations = relationship('Organization', backref='address_associations')


# Сущность Физическое лицо
class Gender(Base):
    __tablename__ = "gender"
    id = Column(Integer, primary_key=True)
    gender = Column(String(7))


class People(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80))
    last_name = Column(String(80))
    patronymic = Column(String(80))
    birth_date = Column(Date)
    gender_id = Column(Integer, ForeignKey(Gender.id), index=True, nullable=False)
    address = relationship('RelationToAddress', secondary='relation_to_address',)

    def __repr__(self):
        return f'People {self.id} {self.last_name} {self.first_name} {self.patronymic} {self.birth_date}'


# Сущность Страховой полис
class TypeOfPolicy(Base):
    __tablename__ = 'type_of_policy'
    id = Column(Integer, primary_key=True)
    type = Column(String)


class NameOfCompany(Base):
    __tablename__ = 'name_of_company'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class InsurancePolicy(Base):
    __tablename__ = 'insurance_policy'
    id = Column(Integer, primary_key=True)
    series = Column(String)
    number = Column(Integer)
    date_of_issue = Column(Date)
    type = Column(Integer, ForeignKey(TypeOfPolicy.id), index=True, nullable=False)
    name_of_company = Column(Integer, ForeignKey(NameOfCompany.id), index=True, nullable=False)

    def __repr__(self):
        return f'<Policy {self.id} {self.series} {self.number}>'


# Сущность Организация
class Organization(Base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    inn = Column(Integer)
    address = relationship('RelationToAddress', secondary='relation_to_address',)
    director = Column(Integer, ForeignKey(People.id), index=True, nullable=False)

    def __repr__(self):
        return f'Организация {self.id} {self.name} {self.inn}'


# Сущность Адрес
class FullAddress(Base):
    __tablename__ = 'full_address'
    id = Column(Integer, primary_key=True)
    address = Column(String)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    full_address = Column(Integer, ForeignKey(FullAddress.id), index=True, nullable=False)
    house_number = Column(Integer)
    building = Column(String(5))
    possession = Column(String(5))
    apartment = Column(Integer)
    peoples = relationship('RelationToAddress', secondary='relation_to_address',)
    organizations = relationship('RelationToAddress', secondary='relation_to_address',)

    def __repr__(self):
        return f'Адрес {self.id} {self.full_address}'


# Сущность Транспортное средство
class ModelAutomobile(Base):
    __tablename__ = 'model_automobile'
    id = Column(Integer, primary_key=True)
    model_automobile = Column(String(100))


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    brand = Column(String(100))


class Color(Base):
    __tablename__ = 'color'
    id = Column(Integer, primary_key=True)
    color = Column(String(100))


class Transport(Base):
    __tablename__ = 'transport'
    id = Column(Integer, primary_key=True)
    reg_number = Column(String(10))
    VIN = Column(String(17))
    brand = Column(Integer, ForeignKey(Brand.id), index=True, nullable=False)
    model_automobile = Column(Integer, ForeignKey(ModelAutomobile.id), index=True, nullable=False)
    color = Column(Integer, ForeignKey(Color.id), index=True, nullable=False)
    owner = Column(Integer, ForeignKey(People.id), index=True, nullable=False)

    def __repr__(self):
        return f'Транспортное средство {self.id} {self.brand} {self.model_automobile} {self.reg_number}'


# Сущность Страховой случай
class InsuranceEvent(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    date_event = Column(Date)
    type_event = Column(String(100))
    participants = Column(Integer, ForeignKey(People.id), index=True, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
