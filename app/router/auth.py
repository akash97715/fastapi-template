from fastapi import FastAPI, Depends, HTTPException, status,APIRouter
from .. import models,schemas,utils,oauth2
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db

routers=APIRouter(tags=["Authentication"])

@routers.post('/login')
def login(user_creds: OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_creds.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="Invalid creds")
    if not utils.verify(user_creds.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid creds")
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"token":access_token,"token_type":"Bearer"}
    


