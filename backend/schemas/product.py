from typing import Optional
from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    # sellerID : Optional[int]
    imgPath: Optional[str] = ""


class GetProduct(Product):
    id: int
    imgPath: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
