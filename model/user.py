from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    national_id = Column(String)
    teleph_number = Column(String)
    email_id = Column(String)
    password = Column(String)
    confirm_password = Column(String)

    def __init__(self, user_id, first_name, last_name, national_id, teleph_number, email_id, password, confirm_password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.teleph_number = teleph_number
        self.email_id = email_id
        self.password = password
        self.confirm_password = confirm_password

    # Getter and setter methods
    def get_user_id(self):
        return self.user_id

    def set_id(self, user_id):
        self.user_id = id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_national_id(self):
        return self.national_id

    def set_national_id(self, national_id):
        self.national_id = national_id

    def get_teleph_number(self):
        return self.teleph_number

    def set_teleph_number(self, teleph_number):
        self.teleph_number = teleph_number

    def get_email_id(self):
        return self.email_id

    def set_email_id(self, email_id):
        self.email_id = email_id

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_confirm_password(self):
        return self.confirm_password

    def set_confirm_password(self, confirm_password):
        self.confirm_password = confirm_password

