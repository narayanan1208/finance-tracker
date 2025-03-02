from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_keys=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    type = Column(String, nullable=False)
    date = Column(Date, nullable=False)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_keys=True, index=True)
    name = Column(String, unique=True, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))