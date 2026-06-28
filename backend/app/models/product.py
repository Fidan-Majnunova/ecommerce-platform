from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Product(Base):
    __tablename__="products"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    price=Column(Float,nullable=False)
    description=Column(String, nullable=False)
    stock=Column(Integer, default=0)
    likes=Column(Integer,default=0)
    category=Column(String,nullable=True)
    image_url=Column(String,nullable=True)
    created_at=Column(DateTime,server_default=func.now())



    