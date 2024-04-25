from fastapi import APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.product import Product 

router = APIRouter(tags=["dealing with products"])

@router.get("/")
def get_items_homepage():
    pass

@router.get("/dashboard")
async def get_products_seler():
    pass

@router.post("/dashboard/additem")
def add_item():
    pass