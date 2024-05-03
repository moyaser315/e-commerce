from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session
from typing import Optional ,Union

from ..database import get_db
from ..models import product as model
from ..models import order as order_model
from ..schemas import product as schema
from ..schemas import orders as order_schema
from .. import oauth

router = APIRouter(prefix="/dashboard", tags=["dealing with products"])


@router.get("/", response_model=Union[schema.GetDashboard , order_schema.OrderDashboard , schema.GetPerson])
async def get_products(
    db: Session = Depends(get_db),
    limit: int = 20,
    page: int = 0,
    search: Optional[str] = "",
    current_user=Depends(oauth.get_current_user),
):
    current_user = schema.GetPerson.model_validate(current_user)
    ret =None
    if current_user.user_type == "seller":
        items = (
            db.query(model.Product)
            .filter(
                model.Product.sellerID == current_user.id,
            )
            .limit(limit=limit)
            .offset(page * limit)
            .all()
        )
        items = [schema.GetProduct.model_validate(item) for item in items]
        ret = schema.GetDashboard(product=items, user_info=current_user)

    else :
        items = (
            db.query(order_model.Order)
            .filter(
                model.Product.name.contains(search),
                order_model.Order.buyerID == current_user.id
            )
            .all()
        )
        if not items :
            ret = schema.GetPerson.model_validate(current_user)
        else :
            items = [order_schema.OrderInfo.model_validate(item) for item in items]
            ret = order_schema.OrderDashboard(user_info=current_user,order_info=items)
        


    
    return ret


@router.post("/additem", response_model=schema.GetProduct)
async def add_item(
    item: schema.Product,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth.get_current_user),
):
    ## TODO : quey first if product exist in user and raise exeption
    new_item = model.Product(
        sellerID=current_user.id, **item.model_dump()
    )  # TODO : sellerID == current_user.id
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth.get_current_user),
):
    query_item = db.query(model.Product).filter(model.Product.id == id)
    del_item = query_item.first()
    if not del_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="404 not found"
        )
    if del_item.sellerID != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    query_item.delete(False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schema.GetProduct)
def update_item(
    id: int,
    item: schema.Product,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth.get_current_user),
):
    query_item = db.query(model.Product).filter(model.Product.id == id)
    new_item = query_item.first()
    if not new_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="404 not found"
        )
    if new_item.sellerID != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not allowed")

    query_item.update(item.model_dump(), synchronize_session=False)
    db.commit()
    return query_item.first()
