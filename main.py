from fastapi import FastAPI
from routers import blog
from utils.db import engine, Base

app = FastAPI()

# Include routers
app.include_router(blog.router)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {
        "message": "Hello World!"
    }
