#!/urs/bin/pyhton3
""""""
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

def State(Base):
  __tablename__ = 'states'
  id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
  name = Column(String(128), nullable=False)
