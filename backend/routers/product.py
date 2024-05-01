from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session
from typing import Optional

from ..database import get_db
from ..models import product as model
from ..models import user as user_type
from ..schemas import product as schema
from .. import oauth

router = APIRouter(prefix="/dashboard", tags=["dealing with products"])


def get_info(db: Session, current_user) -> schema.GetPerson:
    user_info = (
        db.query(user_type.User).filter(current_user.id == user_type.User.id).first()
    )
    return user_info


@router.get("/", response_model=schema.GetDashboard)
async def get_products(
    db: Session = Depends(get_db),
    limit: int = 20,
    page: int = 0,
    search: Optional[str] = "",
    current_user: int = Depends(oauth.get_current_user),
):
    items = (
        db.query(model.Product)
        .filter(
            model.Product.name.contains(search),
            model.Product.sellerID == current_user.id,
        )
        .limit(limit=limit)
        .offset(page * limit)
        .all()
    )

    user_info = get_info(db, current_user)
    items = [schema.GetProduct.model_validate(item) for item in items]
    user_info = schema.GetPerson.model_validate(user_info)
    print(user_info)
    ret = schema.GetDashboard(product=items, user_info=user_info)
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
