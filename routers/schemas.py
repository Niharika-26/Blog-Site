from turtle import title
from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel): # whatever we get from the api
    image_url:str
    title:str
    content:str
    creator:str
    timestamp:datetime

class PostDisplay(BaseModel):
    id:int
    image_url:str
    title:str
    content:str
    creator:str
    timestamp:datetime
    class Config():
        orm_mode=True      #equips you with object-oriented tools to run commands that you would usually run on databases. 


