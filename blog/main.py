from fastapi import FastAPI
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash
from .routers import blog, users, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)

