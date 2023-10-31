from fastapi import FastAPI, Depends, HTTPException, status,APIRouter
from .. import models,schemas,utils
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional, List

routers=APIRouter()
@routers.get("/posts")
def read_root():
    return {"Data": "This is your post"}


@routers.post("/createpost",response_model=schemas.ResponsePost)
def create_posts(new_post: schemas.Post, db: Session = Depends(get_db)):
    post = models.Post(**new_post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post


@routers.get("/post",response_model=List[schemas.ResponsePost])
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()

    print(posts)
    return posts


@routers.get("/sqlalchemy")
def get_post(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()

    return {"Posts": post}


@routers.get("/post/{id}",response_model=schemas.ResponsePost)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)

    return post


@routers.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get_post(id: int, db: Session = Depends(get_db)):
    print(type(id))
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with {id} does not exists ",
        )
    post.delete(synchronize_session=False)
    db.commit()

    return {"Message": f"post with{id} got deleted"}

@routers.put("/post/{id}",response_model=schemas.Post)
def get_post(id: int,new_post: schemas.Post, db: Session = Depends(get_db)):
    print(type(id))
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with {id} does not exists ",
        )
    post_query.update(new_post.dict(),synchronize_session=False)
    db.commit()

    return {"Updated post": post_query.first()}