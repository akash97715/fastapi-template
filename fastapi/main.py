from random import randrange
from typing import Optional
from fastapi import  FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int]=None

mypost=[]

def my_post(id):
    for p in mypost:
        if p["id"] == id:
            return p


@app.get("/")
def read_root():
    return {"Message": "Welcome to my API"}

@app.get("/posts")
def read_root():
    return {"Data": "This is your post"}

@app.post("/createpost")
def create_posts(new_post:Post):
    post=dict(new_post)
    post["id"]=randrange(0,1000000)
    mypost.append(post)
    print(new_post)
    
    return {"data":post}

@app.get("/posts/{id}")
def get_post(id):
    intid=int(id)
    actual_post=my_post(intid)
    return {"Data": actual_post}