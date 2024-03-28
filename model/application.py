from sqlalchemy import Column, Integer, String, ForeignKey,Enum,Numeric,Float
from sqlalchemy.orm import relationship
from model.user import User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum

Base = declarative_base()

class StateAppEnum(PyEnum):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'


class WaterPermitApplication(Base):
    
    __tablename__ = 'water_permit_applicant'

    id = Column(Integer, primary_key=True)
    id_of_app = Column(String)
    full_Name=Column(String)
    applicant_category = Column(String)
    applicant_type=Column(String)
    national_id = Column(String)
    teleph_number = Column(String)
    email_id = Column(String)
    date_app = Column(String) 
    state_app = Column(Enum(StateAppEnum))
    date_app = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)  
    
    def __init__(self, id_of_app, full_name, applicant_category, applicant_type, national_id,
                 teleph_number, email_id, date_app, state_app, user_id):
        self.id_of_app = id_of_app
        self.full_name = full_name
        self.applicant_category = applicant_category
        self.applicant_type = applicant_type
        self.national_id = national_id
        self.teleph_number = teleph_number
        self.email_id = email_id
        self.date_app = date_app
        self.state_app = state_app
        self.user_id = user_id

class WaterDocumentUpload(Base):
    
    __tablename__ = 'water_document_upload'
    
    __tablename__ = 'water_document_upload'
    
    id = Column(Integer, primary_key=True)  # Define a primary key column
    file_name = Column(String)
    file_upload = Column(String)
    water_permit_application_id = Column(Integer, ForeignKey('water_permit_applications.id'))
    water_permit_application = relationship("WaterPermitApplication")
    
    def __init__(self, id_file, file_name, file_upload, water_permit_application):
        self.id_file = id_file
        self.file_name = file_name
        self.file_upload = file_upload
        self.water_permit_application = water_permit_application

class WaterPermitPayment(Base):
    
    __tablename__ = 'water_permit_payment'

    payment_id = Column(Integer, primary_key=True)  # Assuming payment_id is the primary key
    payment_amount = Column(Numeric(precision=10, scale=2))
    payment_type = Column(String)
    water_permit_application_id = Column(Integer, ForeignKey('water_permit_applications.id'))
    water_permit_application = relationship("WaterPermitApplication")
    
    def __init__(self, payment_id, payment_amount, payment_type, water_permit_application):
        self.payment_id = payment_id
        self.payment_amount = payment_amount
        self.payment_type = payment_type
        self.water_permit_application = water_permit_application



