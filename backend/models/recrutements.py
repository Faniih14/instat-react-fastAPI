from sqlalchemy import Column, BigInteger, String, Text, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from db.database import Base

class Recrutement(Base):
    __tablename__ = "recrutements"

    id = Column(BigInteger, primary_key=True, index=True)
    publisher_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    title = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    excerpt = Column(Text)
    body = Column(Text)

    active = Column(Boolean, default=True)
    published_at = Column(TIMESTAMP)

    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    # relation
    publisher = relationship("User", back_populates="recrutements")