from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
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

class WaterCategory(Category):
    __tablename__ = 'water_categories'

    id_water_category = Column(Integer, primary_key=True)
    type_of_water = Column(String)
    use_of_water = Column(String)
    source_of_water = Column(String)

class WaterLocation(Base):
    __tablename__ = 'water_locations'

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
    water_category = relationship(WaterCategory)

# Create engine and tables
engine = create_engine('sqlite:///water_permit.db')
Base.metadata.create_all(engine)
