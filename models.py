from pydantic import BaseModel
from pydantic.networks import EmailStr
from fastapi import Form


class User(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    new_worker: bool = True
    employee: str
    
class Orders(BaseModel):
    email: EmailStr
    
    @classmethod
    def as_form(cls, email: EmailStr = Form(...)):
        return cls(email=email)