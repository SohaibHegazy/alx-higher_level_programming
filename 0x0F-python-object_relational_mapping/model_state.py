#!/usr/bin/python3
'''
a python file that contains the class definition of
a State and an instance Base = declarative_base()
'''
from SQLAlchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''
    Class State to inherit from Base
    Args:
    Base
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)