from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from exercises_db import Base, engine


# Сущность Компания
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    city = Column(String)
    address = Column(String)
    phone = Column(String)
    employees = relationship('Employee', lazy='joined')

    def __repr__(self):
        return f'Организация {self.id} {self.name}'


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey(Company.id), index=True, nullable=False)
    name = Column(String)
    job = Column(String)
    phone = Column(String)
    email = Column(String)
    date_of_birth = Column(Date)
    companies = relationship('Company')

    def __repr__(self):
        return f'People {self.id} {self.name}'


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey(Employee.id), index=True, nullable=False)
    payment_date = Column(Date)
    ammount = Column(Integer)


    def __repr__(self):
        return f'Payment_id: {self.id}, date: {self.payment_date}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
