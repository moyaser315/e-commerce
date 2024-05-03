from typing import List
from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from .person import GetPerson

class CartItems(BaseModel):
    quantity: int
    productID: int
    model_config = ConfigDict(from_attributes=True)
    
class OrderItem(BaseModel):
    productID : int
    quantity : int
    buyPrice : float
    model_config =ConfigDict(from_attributes=True)

class OrderCheckOut(BaseModel):
    order_item: List[OrderItem]
    totalCost : float
    model_config =ConfigDict(from_attributes=True)
    
class OrderInfo(BaseModel) :
    id :int
    totalCost : float
    model_config =ConfigDict(from_attributes=True)
    
class OrderDashboard(BaseModel):
    user_info: GetPerson
    order_info : List[OrderInfo]
    model_config =ConfigDict(from_attributes=True)