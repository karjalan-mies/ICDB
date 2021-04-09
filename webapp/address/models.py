from webapp.db import db

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
