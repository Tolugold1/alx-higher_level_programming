#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """
    Define a State class
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
