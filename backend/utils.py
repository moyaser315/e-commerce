from passlib.context import CryptContext

# generating report
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .schemas import product as schema
from .models import product as model

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return PWD_CONTEXT.hash(password)


def verify(sent_pass, hashed_pass):
    return PWD_CONTEXT.verify(sent_pass, hashed_pass)


def add_seller_elem(file, db, items, current_user, y):
    file.setFont("Helvetica-Bold", 15)
    file.drawString(30, y, "Products for sale")
    y -= 30
    y = add_items_to_report(y, items, file)
    file.setFont("Helvetica-Bold", 15)
    y -= 30
    file.drawString(30, y, "Products Sold")
    y -= 30
    prod = (
        db.query(model.Product).filter(model.Product.sellerID == current_user.id).all()
    )
    l = []
    for p in prod:
        ord = p.orderItems
        q = 0
        for o in ord:
            q += o.quantity
            # print(p.name,p.description,p.price,q,p.cat)
        l.append(
            schema.GetProduct(
                id=p.id,
                name=p.name,
                description=p.description,
                price=p.price,
                quantity=q,
                cat=p.cat,
            )
        )
    y = add_items_to_report(y, l, file)


def add_buyer_elem(file, items, y):
    file.setFont("Helvetica-Bold", 15)
    file.drawString(30, y, "orders purchased")
    y -= 10

    for item in items:
        y -= 20
        file.setFont("Helvetica", 14)
        file.drawString(30, y, f"order id : {item.id}")
        y -= 20
        l = []
        for i in item.orderItems:
            p = schema.GetProduct.model_validate(i.product)
            p.quantity = i.quantity
            l += [p]
        y = add_items_to_report(y, l, file)


def add_user_info(file: canvas.Canvas, current_user, y):
    file.setFont("Helvetica-Bold", 15)
    file.drawString(30, y, "User info")
    y -= 30
    file.setFont("Helvetica", 12)
    file.drawString(30, y, "ID")
    file.drawString(100, y, "Name")
    file.drawString(200, y, "email")
    file.drawString(300, y, "usertype")
    file.drawString(400, y, "balance")
    y -= 20
    file.drawString(30, y, str(current_user.id))
    file.drawString(100, y, current_user.name)
    file.drawString(200, y, str(current_user.email))
    file.drawString(300, y, current_user.user_type)
    file.drawString(400, y, str(current_user.balance))
    y -= 50
    return y


def add_items_to_report(y, products, file: canvas.Canvas):

    file.setFont("Helvetica", 12)
    file.drawString(30, y, "ID")
    file.drawString(100, y, "Name")
    file.drawString(200, y, "Price")
    file.drawString(300, y, "Description")
    file.drawString(400, y, "Category")
    file.drawString(500, y, "Quantity")

    # Initial y-coordinate for product details
    y -= 20

    # Add each product to the report
    for product in products:
        file.drawString(30, y, str(product.id))
        file.drawString(100, y, product.name)
        file.drawString(200, y, str(product.price))
        file.drawString(300, y, product.description)
        file.drawString(400, y, product.cat)
        file.drawString(500, y, str(product.quantity))

        y -= 20  # Move down for next product
    return y
