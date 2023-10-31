from fastapi import FastAPI, Depends, HTTPException, status,APIRouter
from .. import models,schemas,utils
from sqlalchemy.orm import Session
from ..database import get_db

routers=APIRouter()

@routers.post("/createUser",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        hashed_pwd=utils.hash(user.password)
        user.password=hashed_pwd
        post = models.Users(**user.dict())

        db.add(post)
        db.commit()
        db.refresh(post)
        return post

@routers.get("/getUser/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def get_user(id:int, db: Session = Depends(get_db)):
        user=db.query(models.Users).filter(models.Users.id==id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with {id} does not exist")
        
        
        return user