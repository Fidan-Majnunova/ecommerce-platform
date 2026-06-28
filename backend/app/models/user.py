from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func   #I imported func only for NOW() function of SQL, so PostgreSQL will automatically write the current time 
from app.database import Base

class User(Base):
    __tablename__= "users"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, Nullible=False)
    email=Column(String,unique=True, Nullible=False)
    password=Column(String, Nullible=False)
    is_admin=Column(Boolean, default=False)
    created_at=Column(DateTime, server_default=func.now())

