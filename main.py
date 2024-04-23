from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from database import engine, Base, get_db
from models import user, buyer, seller, product, comment, cartItem, orderItem, order


# Setup
app =FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/")
def root(db: Session = Depends(get_db)):
    # user = seller.Seller(name = "Sayed", email = "mahmoud@gmail.com", password = "123456")
    # db.add(user)
    # db.commit()
    # db.refresh(user)
    
    # prod = product.Product(name = "lol", description = "toxic", price = 1, quantity = 2, sellerID = user.id)
    # db.add(prod)
    # db.commit()
    # db.refresh(prod)
    
    # comm = comment.Comment(text = "lol", userID = user.id, productID = prod.id)
    # db.add(comm)
    # db.commit()
    # db.refresh(comm)
    
    # item = cartItem.CartItem(productID = prod.id, buyerID = user.id, quantity = 1)
    # db.add(item)
    # db.commit()
    # db.refresh(item)
    
    # ord = order.Order(buyerID = user.id)
    # db.add(ord)
    # db.commit()
    # db.refresh(ord)
    
    # oitem = orderItem.OrderItem(quantity = 1, buyPrice = 2, productID = prod.id, orderID = ord.id)
    # db.add(oitem)
    # db.commit()
    # db.refresh(oitem)
    
    return "buyer"


