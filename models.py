import os 
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Thanks(Base):
	__tablename__ = 'Thanks'
	id = Column(Integer, primary_key=True)
	email = Column(String(250), nullable=False)
	message = Column(String(4000), nullable=False)

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)