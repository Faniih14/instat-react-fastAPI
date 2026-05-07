from sqlalchemy import Integer,String,Date,Column,DateTime,BigInteger
from db.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=True)
    email = Column(String(191), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    remember_token = Column(String(100), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

     # relations
    pages = relationship("Page", back_populates="author")
    recrutements = relationship("Recrutement", back_populates="publisher")
    posts = relationship("Post", back_populates="author")