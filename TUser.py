from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the SQLAlchemy base class
Base = declarative_base()

# Define a sample model
class TUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create an engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Create the tables in the database
Base.metadata.create_all(engine)

# Example usage
user = TUser(name='John')
print(user.name)
