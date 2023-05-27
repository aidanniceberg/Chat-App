from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column("firstName", String)
    last_name = Column("lastName", String)
    password = Column("pw", String)
    birthday = Column(DateTime)
    email = Column(String)