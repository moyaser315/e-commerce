from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from .person import GetPerson


class Product(BaseModel):

    name: str
    description: str
    price: float
    quantity: int
    cat: str | None = "devices"
    imgPath: str | None = ""


class GetProduct(Product):
    id: int
    model_config = ConfigDict(from_attributes=True)
    quantity_sold: int | None = 0


class GetDashboard(BaseModel):
    product: List[GetProduct]
    user_info: GetPerson
    model_config = ConfigDict(from_attributes=True)
