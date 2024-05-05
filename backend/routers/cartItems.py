from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import cartItem as model
from ..models import user as user_model
from ..schemas import orders as schema
from ..schemas import person as user_scheme
from .. import oauth

router = APIRouter(prefix="/cart", tags=["Cart Item"])


@router.get("", response_model=List[schema.CartItems])
async def get_products(
    db: Session = Depends(get_db),
    limit: int = 20,
    page: int = 0,
    current_user=Depends(oauth.get_current_user),
):
    current_user = user_scheme.GetPerson.model_validate(current_user)

    items = (
        db.query(model.CartItem)
        .filter(model.CartItem.buyerID == current_user.id)
        .limit(limit=limit)
        .offset(page * limit)
        .all()
    )

    return items


@router.put("")
async def update_cart(
    data: schema.CartItems,
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(oauth.get_current_user),
) -> schema.CartItems:
    if current_user.user_type == "seller":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="you can't buy items",
        )
        
    if (data.quantity < 0):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid quantity")
    
            
    prod = (
        db.query(model.Product).filter(model.Product.id == data.productID).first()
    )

    if not prod:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="non existent product"
        )
        
    if data.quantity > prod.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The quantity you ordered exceed the available quantity by {data.quantity - prod.quantity}",
        )
        
    cart_item = (
        db.query(model.CartItem)
        .filter(
            model.CartItem.buyerID == current_user.id,
            model.CartItem.productID == data.productID,
        )
        .first()
    )
    
    remove: bool = False
    if cart_item:
        diff: int = data.quantity - cart_item.quantity
        if diff > prod.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"The quantity you ordered exceed the available quantity by {diff}",
            )
            
        cart_item.quantity += diff
        if (cart_item.quantity == 0):
            remove = True
            
    else:
        if (data.quantity == 0):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Can't add new cart item with quantity 0"
            )
            
        cart_item = model.CartItem(buyerID=current_user.id, **data.model_dump())
        db.add(cart_item)
            
    if (remove):
        db.delete(cart_item)

    db.commit()
    if not remove:
        db.refresh(cart_item)
    
    return cart_item


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_item(
#     id: int,
#     db: Session = Depends(get_db),
#     current_user: int = Depends(oauth.get_current_user),
# ):
#     query_item = db.query(model.CartItem).filter(model.CartItem.productID == id)
#     del_item = query_item.first()
#     if not del_item:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="404 not found"
#         )
#     if del_item.buyerID != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#     pro = db.query(model.Product).filter(model.Product.id == del_item.productID).first()
#     pro.quantity += del_item.quantity
#     query_item.delete(False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.put("/{id}", response_model=schema.CartItems)
# def update_item(
#     id: int,
#     item: schema.CartItems,
#     db: Session = Depends(get_db),
#     current_user: int = Depends(oauth.get_current_user),
# ):
#     query_item = db.query(model.CartItem).filter(model.CartItem.productID == id)
#     new_item = query_item.first()

#     orig_quan = (
#         db.query(model.Product).filter(model.Product.id == item.productID).first()
#     )
#     if not new_item:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="404 not found"
#         )
#     if new_item.buyerID != current_user.id:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not allowed")

#     if item.quantity > orig_quan.quantity or item.quantity < 1:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=f"The quantity you ordered isn't allowed",
#         )
#     new_item.quantity = item.quantity
#     db.commit()
#     return query_item.first()
