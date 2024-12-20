from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.blogs import Blog, BlogCreate, BlogResponse
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


@router.get("/blogs", response_model=list[BlogResponse])
def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@router.get("/blog:id", response_model=BlogResponse)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query("Select * from blogs where id = :id", id=id).first()
    return blog


@router.put("/blog:id")
def update_blog(id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    blog = db.query("Update from blogs where id = :id", id=id).first()
    return blog


@router.delete("/blog:id")
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query("Delete from blogs where id = :id", id=id).first()
    return blog