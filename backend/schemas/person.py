from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict ,EmailStr



class PersonBase(BaseModel) :
    name: str
    email: EmailStr
    mobile : str
    user_type : str

class CreatePerson(PersonBase):
    password: str

    

class GetPerson(PersonBase):
    model_config = ConfigDict(from_attributes=True)
    id : int

    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    
    