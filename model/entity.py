from sqlalchemy import create_engine, Column, Integer, String, Float,Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Entity(Base):
    __tablename__ = 'entities'

    id_entity = Column(Integer, primary_key=True)
    entity_name = Column(String)
    tin_number = Column(String)

class Category(Base):
    __tablename__ = 'categories'

    id_category = Column(Integer, primary_key=True)
    category_name = Column(String)
    entity_id = Column(Integer, ForeignKey('entities.id_entity'))
    entity = relationship(Entity)

class WaterSourceCategory(Base):
    __tablename__ = 'water_source_category'

    water_category_id = Column(Integer, primary_key=True)
    water_source_type = Column(String)   	
    water_source_name = Column(String)
    water_land_use_owner=Column(Boolean)
    water_intended_activities = Column(String)
    
    def __init__(self, water_source_type, water_source_name, water_land_use_owner, water_intended_activities):
        self.water_source_type = water_source_type
        self.water_source_name = water_source_name
        self.water_land_use_owner = water_land_use_owner
        self.water_intended_activities = water_intended_activities

class WaterPermitLocation(Base):
    __tablename__ = 'water_permit_location'

    id_location = Column(Integer, primary_key=True)
    province = Column(String)
    district = Column(String)
    sector = Column(String)
    cell = Column(String)
    village = Column(String)
    street = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    water_category_id = Column(Integer, ForeignKey('water_categories.id_water_category'))
    water_category = relationship(WaterSourceCategory)
    
    def __init__(self, province, district, sector, cell, village, street, latitude, longitude, water_category_id):
        self.province = province
        self.district = district
        self.sector = sector
        self.cell = cell
        self.village = village
        self.street = street
        self.latitude = latitude
        self.longitude = longitude
        self.water_category_id = water_category_id