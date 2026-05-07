from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, BigInteger, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    author_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    #id_category = Column(BigInteger, ForeignKey("categories.id"), nullable=True)
    #id_region = Column(BigInteger, ForeignKey("regions.id"), nullable=True)
    
    title = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    excerpt = Column(Text, nullable=True)
    body = Column(Text, nullable=True)
    image = Column(String(255), nullable=True)
    
    level = Column(String(255), nullable=True)
    type_post = Column(String(255), nullable=True)
    
    banner = Column(Boolean, default=0)
    text_color = Column(String(50), nullable=True)
    attachments = Column(Text, nullable=True)
    last_nipc_publication = Column(Boolean, default=0)
    active = Column(Boolean, default=1)
    
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    # Relation
    author = relationship("User", back_populates="posts")
    #category = relationship("Category", back_populates="posts")
    #region = relationship("Region", back_populates="posts")

    #post_files = relationship("PostFile", back_populates="post", cascade="all, delete")