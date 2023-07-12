from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from .. import schemas, database, models, hashing
from typing import List
from sqlalchemy.orm import Session
from ..repository import users


get_db = database.get_db


router = APIRouter(
    prefix= '/user',
    tags=['users']
)



@router.post('/', response_model=schemas.ShowUser)
def create_user(request :schemas.User, db: Session = Depends(get_db)):
    return users.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id, db: Session = Depends(get_db) ):
    return users.show(id,db)
