from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Order(Base):
    __tablename__="orders"
    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    status = Column(String, nullable=False)
    ordered_At = Column(DateTime, server_default=func.now())
    total_price = Column(Float, default=0)
    quantity = Column(Integer, nullable=False)

