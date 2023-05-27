from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Threads(Base):
    __tablename__ = "threads"
    
    id = Column(Integer, primary_key=True)
    user1 = Column(Integer)
    user2 = Column(Integer)