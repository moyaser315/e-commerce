from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import cartItem as cart_model
from ..models import order, orderItem, seller
from ..schemas import orders as schema
from ..schemas import person as user_scheme
from .. import oauth
from ..sender import send_emails_to_sellers


router = APIRouter(prefix="/checkout", tags=["checkout"])


@router.get("", response_model=schema.OrderCheckOut)
async def get_products(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user=Depends(oauth.get_current_user),
):

    items_query = db.query(cart_model.CartItem).filter(
        cart_model.CartItem.buyerID == current_user.id
    )
    items = items_query.all()
    if not items:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="please add items to cart first",
        )
    cur_order = order.Order(buyerID=current_user.id, totalCost=0)
    db.add(cur_order)
    db.commit()
    db.refresh(cur_order)

    orders = {}
    for item in items:
        item = schema.CartItems.model_validate(item)

        pr = (
            db.query(cart_model.Product)
            .filter(item.productID == cart_model.Product.id)
            .first()
        )

        if item.quantity > pr.quantity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"invalid quantity for {pr.name}, current quantity is {pr.quantity}",
            )

        new_item = orderItem.OrderItem(
            buyPrice=pr.price, orderID=cur_order.id, **item.model_dump()
        )

        pr.quantity -= item.quantity

        seller_user = (
            db.query(seller.Seller).filter(pr.sellerID == seller.Seller.id).first()
        )

        cost = new_item.buyPrice * new_item.quantity
        seller_user.balance += cost
        cur_order.totalCost += cost
        db.add(new_item)

        exists = orders.get(seller_user.email)
        if exists:
            orders[seller_user.email].append(
                {"id": pr.id, "product name": pr.name, "quantity": new_item.quantity}
            )
        else:
            orders[seller_user.email] = [
                {"id": pr.id, "product name": pr.name, "quantity": new_item.quantity}
            ]

    # current_user.balance -= cur_order.totalCost
    items_query.delete(False)
    db.commit()
    db.refresh(cur_order)
    print(current_user.email, current_user.balance)

    cur_order_items = cur_order.orderItems
    cur_order_items = [
        schema.OrderItem.model_validate(item) for item in cur_order_items
    ]

    cur_order = schema.OrderCheckOut.model_validate(
        {
            "totalCost": cur_order.totalCost,
            "order_item": cur_order_items,
            "id": cur_order.id,
        }
    )

    try:
        background_tasks.add_task(
            send_emails_to_sellers, orders, cur_order.id, current_user.email
        )
    except:
        pass

    return cur_order
