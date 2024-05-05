from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session
from typing import Optional, Union

from ..database import get_db
from ..models import product as model
from ..models import order as order_model
from ..schemas import product as schema
from ..schemas import orders as order_schema
from ..models import user as user_model
from .. import oauth

router = APIRouter(prefix="/dashboard", tags=["dealing with dashboard"])


@router.get(
    "",
    response_model=Union[
        schema.GetDashboard, order_schema.OrderDashboard, schema.GetPerson
    ],
)
async def get_products(
    db: Session = Depends(get_db),
    limit: int = 20,
    page: int = 0,
    search: Optional[str] = None,
    cat: Optional[str] = None,
    current_user: user_model.User=Depends(oauth.get_current_user),
):
    current_user = schema.GetPerson.model_validate(current_user)
    ret = None
    if current_user.user_type.lower() == "seller":
        if cat and search:
            items = (
                db.query(model.Product)
                .filter(model.Product.sellerID == current_user.id, model.Product.cat == cat, model.Product.name.contains(search))
                .order_by(model.Product.id)
                .limit(limit=limit)
                .offset(page * limit)
                .all()
            )
        
        elif search:
            items = (
                db.query(model.Product)
                .filter(model.Product.sellerID == current_user.id, model.Product.name.contains(search))
                .order_by(model.Product.id)
                .limit(limit=limit)
                .offset(page * limit)
                .all()
            )
            
        elif cat:
            items = (
                db.query(model.Product)
                .filter(model.Product.sellerID == current_user.id, model.Product.cat == cat)
                .order_by(model.Product.id)
                .limit(limit=limit)
                .offset(page * limit)
                .all()
            )
        
        else:
            items = (
                db.query(model.Product)
                .filter(model.Product.sellerID == current_user.id)
                .order_by(model.Product.id)
                .limit(limit=limit)
                .offset(page * limit)
                .all()
            )
            
        items = [schema.GetProduct.model_validate(item) for item in items]
        ret = schema.GetDashboard(product=items, user_info=current_user)
    else:
        items = (
            db.query(order_model.Order)
            .filter(
                order_model.Order.buyerID == current_user.id,
            )
            .order_by(desc(order_model.Order.id))
            .all()
        )
        
        if not items:
            ret = schema.GetPerson.model_validate(current_user)
        else:
            items = [order_schema.OrderInfo.model_validate(item) for item in items]
            ret = order_schema.OrderDashboard(user_info=current_user, order_info=items)

    return ret


@router.post("/additem", response_model=schema.GetProduct)
async def add_item(
    item: schema.Product,
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(oauth.get_current_user),
):

    if current_user.user_type.lower() != "seller":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not allowed")
    # pro = db.query(model.Product).filter(model.Product.name == item.name)
    new_item = model.Product(sellerID=current_user.id, **item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(oauth.get_current_user),
):
    if current_user.user_type.lower() != "seller":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not allowed")
    
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


@router.patch("/{id}", response_model=schema.GetProduct)
def update_item(
    id: int,
    item: schema.Product,
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(oauth.get_current_user),
):
    if current_user.user_type.lower() != "seller":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not allowed")
    
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


@router.get("/{id}", response_model=order_schema.OrderCheckOut)
async def get_order(
    id: int, db: Session = Depends(get_db), current_user: user_model.User =Depends(oauth.get_current_user)
):  # TODO: is it for buyer only?
    current_user = schema.GetPerson.model_validate(current_user)
    ret = None

    items = db.query(order_model.Order).filter(order_model.Order.id == id).first()
    print(items.id)
    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="please use the interface"
        )
    cur_order_items = items.orderItems
    cur_order_items = [
        order_schema.OrderItem.model_validate(item) for item in cur_order_items
    ]
    ret = order_schema.OrderCheckOut.model_validate(
        {"totalCost": items.totalCost, "order_item": cur_order_items, "id": items.id}
    )

    return ret
