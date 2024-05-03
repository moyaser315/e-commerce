from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import cartItem as cart_model
from ..models import order, orderItem, seller
from ..schemas import orders as schema
from ..schemas import person as user_scheme
from .. import oauth

router = APIRouter(prefix="/checkout", tags=["checkout"])


@router.get("/", response_model=schema.OrderCheckOut)
async def get_products(
    db: Session = Depends(get_db),
    current_user=Depends(oauth.get_current_user),
):

    items = (
        db.query(cart_model.CartItem)
        .filter(cart_model.CartItem.buyerID == current_user.id)
        .all()
    )
    cur_order = order.Order(buyerID=current_user.id, totalCost=1.0)
    db.add(cur_order)
    db.commit()
    db.refresh(cur_order)

    for item in items:
        item = schema.CartItems.model_validate(item)

        pr = (
            db.query(cart_model.Product)
            .filter(item.productID == cart_model.Product.id)
            .first()
        )
        new_item = orderItem.OrderItem(
            buyPrice=pr.price, orderID=cur_order.id, **item.model_dump()
        )

        seller_user = (
            db.query(seller.Seller).filter(pr.sellerID == seller.Seller.id).first()
        )
        cost = new_item.buyPrice * new_item.quantity
        seller_user.balance += cost
        cur_order.totalCost += cost
        db.add(new_item)

    current_user.balance -= cur_order.totalCost
    db.commit()
    db.refresh(cur_order)
    print(current_user.email, current_user.balance)
    cur_order_items = cur_order.orderItems
    cur_order_items = [
        schema.OrderItem.model_validate(item) for item in cur_order_items
    ]

    cur_order = schema.OrderCheckOut.model_validate(
        {"totalCost": cur_order.totalCost, "order_item": cur_order_items}
    )
    return cur_order
