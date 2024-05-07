from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session
from typing import List, Optional, Union

from ..database import get_db
from ..models import product as model
from ..models import order as order_model
from ..schemas import product as schema
from ..schemas import orders as order_schema
from ..models import user as user_model
from ..models import seller as seller_model
from ..models import buyer as buyer_model
from .. import oauth
from .. import utils

# generating report
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


router = APIRouter(prefix="/report", tags=["dealing with reports"])


@router.get("/")
async def get_products(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(oauth.get_current_user),
):
    current_user = schema.GetPerson.model_validate(current_user)
    pdf_filename = None
    items = None
    if current_user.user_type.lower() == "seller":
        items = (
            db.query(seller_model.Seller)
            .filter(current_user.id == seller_model.Seller.id)
            .first()
        )
        items = items.products
        pdf_filename = f"products_{current_user.id}.pdf"
    else:
        print("here")
        items = (
            db.query(buyer_model.Buyer)
            .filter(current_user.id == buyer_model.Buyer.id)
            .first()
        )
        items = items.orders
        pdf_filename = f"orders_{current_user.id}.pdf"

    file = canvas.Canvas(pdf_filename, pagesize=letter)

    file.setFont("Helvetica", 12)

    # Title
    y = 770
    file.setFont("Helvetica-Bold", 20)
    file.drawString(220, y, "Activity Report")
    y -= 50
    y = utils.add_user_info(file, current_user, y)

    if pdf_filename[0] == "p":
        file.setFont("Helvetica-Bold", 15)
        file.drawString(30, y, "Products for sale")
        y -= 30
        y = utils.add_items_to_report(y, items, file)
    else:
        file.setFont("Helvetica-Bold", 15)
        file.drawString(30, y, "orders purchased")
        y -= 30
        
        for item in items:
            file.setFont("Helvetica", 14)
            file.drawString(30, y, f"order id : {item.id}")
            y -= 20
            l = []
            for i in item.orderItems:
                
                l+=[schema.GetProduct.model_validate(i.product)]
            y=utils.add_items_to_report(y,l,file)

    file.save()

    # Return the path to the PDF file
    return pdf_filename
