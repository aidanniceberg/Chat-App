from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Messages(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True)
    is_group = Column("isGroup", Boolean)
    thread_id = Column("threadId", Integer)
    sender = Column(Integer)
    content = Column(String)
    timestamp = Column("timeSent", DateTime)
