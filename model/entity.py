from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Entity(Base):
    __tablename__ = 'entities'

    idEntity = Column(Integer, primary_key=True)
    entityName = Column(String)
    tinNumber = Column(String)

class Category(Base):
    __tablename__ = 'categories'

    idCategory = Column(Integer, primary_key=True)
    name = Column(String)
    entity_id = Column(Integer, ForeignKey('entities.idEntity'))
    entity = relationship(Entity)

class WaterCategory(Category):
    __tablename__ = 'water_categories'

    idWaterCategory = Column(Integer, primary_key=True)
    typeOfWater = Column(String)
    useOfWater = Column(String)
    sourceOfWater = Column(String)

class WaterLocation(Base):
    __tablename__ = 'water_locations'

    idLocation = Column(Integer, primary_key=True)
    province = Column(String)
    district = Column(String)
    sector = Column(String)
    cell = Column(String)
    village = Column(String)
    street = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    water_category_id = Column(Integer, ForeignKey('water_categories.idWaterCategory'))
    water_category = relationship(WaterCategory)

# Create engine and tables
engine = create_engine('sqlite:///water_permit.db')
Base.metadata.create_all(engine)
