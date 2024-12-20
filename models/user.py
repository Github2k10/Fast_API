from sqlalchemy import Column, Integer, String, Boolean
from utils.db import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    
class BaseUser(BaseModel):
    username: str
    email: str
    password: str
    

class UserCreate(BaseUser):
    pass
    
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    
    class Config:
        orm_mode = True
        

class UserLogin(BaseModel):
    username: str
    password: str