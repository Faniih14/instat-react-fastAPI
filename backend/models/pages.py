from sqlalchemy import Column, BigInteger, String, Text, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from db.database import Base

class Page(Base):
    __tablename__ = "pages"

    id = Column(BigInteger, primary_key=True, index=True)
    author_id = Column(BigInteger, ForeignKey("users.id"))
    title = Column(String(255), nullable=False)
    parent_slug = Column(String(255))
    slug = Column(String(255), nullable=False)
    body = Column(Text)
    active = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    # relation
    author = relationship("User", back_populates="pages")