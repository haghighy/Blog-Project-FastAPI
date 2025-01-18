from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from typing import List
from passlib.context import CryptContext
from ..repository import user

get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/',response_model=schemas.ShowUser)
def creat_user(request:schemas.User, db:Session=Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,  db:Session=Depends(get_db)):
    return user.show(id, db)
