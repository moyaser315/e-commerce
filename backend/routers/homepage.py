from typing import Optional ,List
from fastapi import APIRouter,HTTPException,status ,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import product as model
from ..schemas import product as schema

router = APIRouter(tags=["Home page viewing products"])

@router.get("/" , response_model= List[schema.GetProduct])
def get_items_homepage(
    db: Session = Depends(get_db) ,
    limit:int =20 ,
    page: int =0 ,
    search: Optional[str] =""
    ):
    items = db.query(model.Product).filter(
        model.Product.name.contains(search)
        ).limit(limit=limit).offset(page*limit).all()
    return items


@router.get("/{id}", response_model=schema.GetProduct)  # id --> path paramater
def get_product(
    id: int, db: Session = Depends(get_db)
): 
    item = db.query(model.Product).filter(model.Product.id == id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="404 not found"
        )

    return item
    