from sqlalchemy import Column, ForeignKey, Integer,BigInteger
from sqlalchemy.orm import relationship
from db.database import Base

class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)

    role = relationship("Role", back_populates="users")