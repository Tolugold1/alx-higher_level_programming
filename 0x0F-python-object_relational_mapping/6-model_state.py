#!/usr/bin/python3
"""
class definition of a State and an instance
 Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """define state"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True, 
                nullable=False, primary_key="True")
    name = Column(String(128), nullable=False)
