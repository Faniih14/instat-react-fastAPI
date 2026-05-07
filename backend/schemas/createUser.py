from pydantic import BaseModel,EmailStr

class CreateUser (BaseModel):
    name:str=None
    firstname:str=None
    email:EmailStr=None
    password:str=None