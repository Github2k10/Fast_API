from sqlalchemy import Column, Integer, String, Boolean
from utils.db import Base
from pydantic import BaseModel

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(String(1000))
    published = Column(Boolean, default=False)


# Base schema for Blog
class BlogBase(BaseModel):
    title: str
    content: str

# Schema for creating a Blog
class BlogCreate(BlogBase):
    pass

# Schema for response, including the ID
class BlogResponse(BlogBase):
    id: int
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True