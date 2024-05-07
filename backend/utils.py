from passlib.context import CryptContext

# generating report
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .schemas import person

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return PWD_CONTEXT.hash(password)


def verify(sent_pass, hashed_pass):
    return PWD_CONTEXT.verify(sent_pass, hashed_pass)


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

    # Initial y-coordinate for product details
    y -= 20

    # Add each product to the report
    for product in products:
        file.drawString(30, y, str(product.id))
        file.drawString(100, y, product.name)
        file.drawString(200, y, str(product.price))
        file.drawString(300, y, product.description)
        file.drawString(400, y, product.cat)
        y -= 20  # Move down for next product
    return y
