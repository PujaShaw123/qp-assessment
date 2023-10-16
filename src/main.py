"""Main File"""

# General Imports
from fastapi import FastAPI
from .database import Base, engine
from .routes import app_router

Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()

# Import App router
app.include_router(app_router.router)
