from sqlalchemy import Column, Integer, String, Float
from .database import Base
from sqlalchemy.orm import relationship 

class UserData(Base):
    __tablename__ = "UserDetails"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    Email = Column(String(255))
    phone = Column(Float, nullable=False)  # 🔹 Float rakho, kyunki price decimal ho sakta hai
    address = Column(String(255),nullable=False) 



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(100), nullable=False)

