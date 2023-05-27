from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Messages(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True)
    group = Column(Boolean)
    thread_id = Column(Integer)
    sender = Column(Integer)
    content = Column(String)
    timestamp = Column(DateTime)
