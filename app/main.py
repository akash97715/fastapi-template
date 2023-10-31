from random import randrange
from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app import models,schemas,utils
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .router import post,user,auth



models.Base.metadata.create_all(bind=engine)

app = FastAPI()








mypost = []


def my_post(id):
    for p in mypost:
        if p["id"] == id:
            return p


def conn_creator():
    while True:
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="fastapi",
                user="postgres",
                password="akash123",
                cursor_factory=RealDictCursor,
            )
            cursor = conn.cursor()
            print("database connection is successfull", cursor)
            break
        except Exception as error:
            print("Connecting to database failed", cursor)
            print("ERROR:", error)
            time.sleep(2)
    return cursor


app.include_router(post.routers)
app.include_router(user.routers)
app.include_router(auth.routers)

@app.get("/")
def read_root():
    return {"Message": "Welcome to my API"}







