from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GroupThreads(Base):
    __tablename__ = "groupThreads"
    
    id = Column(Integer, primary_key=True)
    users = Column(String)