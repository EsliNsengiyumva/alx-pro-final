from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from user import User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class WaterPermitApplication(Base):
    __tablename__ = 'water_permit_applications'

    id = Column(Integer, primary_key=True)
    id_of_app = Column(String)
    permit_representative = Column(String)
    permit_ownership = Column(String)
    intended_activities = Column(String)
    state_app = Column(Enum(String))
    date_app = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)  # Establishing a relationship with User model
    

class FileStorage(Base):
    __tablename__ = 'file_storages'

    id = Column(Integer, primary_key=True)
    id_file = Column(String)
    file_type = Column(String)
    file_name = Column(String)
    file_upload = Column(String)
    water_permit_application_id = Column(Integer, ForeignKey('water_permit_applications.id'))
    water_permit_application = relationship("WaterPermitApplication")

class WaterPermitPayment(Base):
    __tablename__ = 'water_permit_payments'

    id = Column(Integer, primary_key=True)
    payment_id = Column(String)
    payment_amount = Column(Integer)
    payment_paid = Column(Integer)
    payment_detail = Column(String)
    payment_date = Column(String)
    water_permit_application_id = Column(Integer, ForeignKey('water_permit_applications.id'))
    water_permit_application = relationship("WaterPermitApplication")

class Status(Enum):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'




