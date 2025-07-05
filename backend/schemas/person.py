from pydantic import BaseModel, ConfigDict, EmailStr


class PersonBase(BaseModel):
    name: str
    email: EmailStr
    user_type: str
    balance: float | None = 0.0


class CreatePerson(PersonBase):
    password: str


class GetPerson(PersonBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None
