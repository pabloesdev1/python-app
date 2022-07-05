from pydantic import BaseModel

class User(BaseModel):
    _id: str
    name: str
    lastname: str
    email: str
    password: str
