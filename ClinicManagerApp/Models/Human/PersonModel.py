from sqlalchemy import Column, String, Boolean, DateTime, Integer

from ClinicManagerApp import db


class PersonModel(db.Model):
    __tablename__ = 'person_model'
    __abstract__ = True
    first_name = Column(String(20), default='')
    middle_name = Column(String(40), default='')
    last_name = Column(String(20), default='')
    date_of_birth = Column(DateTime())
    address = Column(String(100), default='')
    email = Column(String(50), default='')
    phone_number = Column(String(12), default='')
    sex = Column(Boolean, default=True)

