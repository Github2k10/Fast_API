from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.model import Blog, BlogCreate, BlogResponse
from utils.db import get_db

router = APIRouter()

@router.post("/addBlog", response_model=BlogResponse)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    # Create a new Blog object
    db_blog = Blog(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


@router.post("/blogs", response_model=list[BlogResponse])
def get_blog(db: Session = Depends(get_db)):
    """Get all blogs"""
    blogs = db.query(Blog).all()
    return blogs