from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict ,EmailStr





class CreatePerson(BaseModel):
   # model_config = ConfigDict(from_attributes=True)
    name: str
    email: EmailStr
    password: str
    

class GetPerson(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name:str
    email: EmailStr
    created_at : datetime
    
class Token(BaseModel):
    access_token: str
    token_type : Optional[str] = "Bearer"
    
    