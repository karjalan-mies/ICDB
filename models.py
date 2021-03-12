from sqlalchemy import Column, Integer, String, Date
from db import Base, engine

'''  Сущность "Физические лица"  '''
class People(Base):
    __tablename__ = 'peoples'
    id_people = Column(Integer, primary_key=True)
    first_name = Column(String(80))
    last_name = Column(String(80))
    patronymic = Column(String(80))
    birth_date = Column(Date)
    gender = Column(Integer)  #Внешний ключ на таблицу 'gender'
    address = Column(Integer)  #Внешний ключ на таблицу 'relation_to_addres'

    def __repr__(self):
        return f'People {self.id_people} {self.last_name} {self.first_name} {self.patronymic} {self.birth_date}'

class Gender(Base):
    __tablename__ = 'gender'
    id_gender = Column(Integer, primary_key=True)
    gender = Column(String(7))

class RelationToAddress(Base):
    __tablename__ = 'relation_from_people_to_address'
    id_relation = Column(Integer, primary_key=True)
    type_relation = Column(Integer)  #Внешний клчю на таблицу 'type_relation'
    people = Column(Integer)  #Внешний клчю на таблицу 'people'
    address = Column(Integer)  #Внешний клчю на таблицу 'address'

class TypeRelation(Base):
    __tablename__ = 'type_relation'
    id_type_relation = Column(Integer, primary_key=True)
    type_relation = Column(String(100))  #Проживает, Зарегистрирован, Ранее проживал, Ранее был зарегистрирован

'''  Сущность "Страховой полис"  '''
class InsurancePolicy(Base):
    __tablename__ = 'insurance_policy'
    id_policy = Column(Integer, primary_key=True)
    series = Column(String)
    number = Column(Integer)
    date_of_issue = Column(Date)
    type = Column(Integer)  # Внешний ключ на таблицу "type_of_policy"
    name_of_company = Column(Integer)  #Внешний ключ на таблицу 'name_of_company'

    def __repr__(self):
        return f'<Policy {self.id_policy} {self.series} {self.number}>'

class TypeOfPolicy(Base):
    __tablename__ = 'type_of_policy'
    id_type_of_policy = Column(Integer, primary_key=True)
    type = Column(String)

class NameOfCompany(Base):
    __tablename__ = 'name_of_company'
    id_name_of_company = Column(Integer, primary_key=True)
    name = Column(String)

'''  Сущность "Организация" '''
class Organization(Base):
    __tablename__ = 'organization'
    id_organization = Column(Integer, primary_key=True)
    name = Column(String(300))
    inn = Column(Integer)
    address = Column(Integer)  #Внешний ключ на таблицу 'Адреса'
    director = Column(Integer)  #Внешний ключ на таблицу 'Peoples'

    def __repr__(self):
        return f'Организация {self.id_organization} {self.name} {self.inn}'

'''  Сущность "Адреса"  '''
'''
Будет простой словарь, где каждому дому будет соответствовать одна запись, содержащая субъект, город, район и улицу.
В дальнейшем можно переделать в составной словарь, где субъект, город, район и улица будут самостоятельными словарями
'''
class Address(Base):              #
    __tablename__ = 'address'     #
    id_address = Column(Integer, primary_key=True)  #
    full_address = Column(Integer)
    house_number = Column(Integer)
    building = Column(String(5))
    possession = Column(String(5))
    apartment = Column(Integer)

    def __repr__(self):
        return f'Адрес {self.id_address} {self.full_address}'

class FullAddress(Base):
    __tablename__ = 'full_address'
    id_full_address = Column(Integer, primary_key=True)
    address = Column(String)

'''  Сущность "Транспортное средство"  '''
class Transport(Base):
    __tablename__ = 'transport'
    id_transport = Column(Integer, primary_key=True)
    reg_number = Column(String(10))
    VIN = Column(String(17))
    brand = Column(Integer)  #Внешний ключ на таблицу 'brand'
    model = Column(Integer)  #Внешний ключ на таблицу 'model'
    color = Column(Integer)  #Внешний ключ на таблицу 'color'
    owner = Column(Integer)  #Внешний ключ на таблицу 'peoples'

    def __repr__(self):
        return f'Транспортное средство {self.id_transport} {self.brand} {self.model} {self.reg_number}'

class Model(Base):
    __tablename__ = 'model'
    id_model = Column(Integer, primary_key=True)
    model = Column(String(100))

class Brand(Base):
    __tablename__ = 'brand'
    id_brand = Column(Integer, primary_key=True)
    brand = Column(String(100))

class Color(Base):
    __tablename__ = 'color'
    id_color = Column(Integer, primary_key=True)
    color = Column(String(100))

'''  Сущность "Страховой случай"  '''
class InsuranceEvent(Base):
    __tablename__ = 'event'
    id_event = Column(Integer, primary_key=True)
    date_event = Column(Date)
    type_event = Column(String(100))
    participants = Column(Integer)  #Внешний ключ на таблицу "people" и "organization"

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)