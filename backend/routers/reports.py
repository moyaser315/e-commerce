import os
from fastapi import APIRouter, HTTPException, Response, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import desc
from sqlalchemy.orm import Session
from typing import List, Optional, Union

from ..database import get_db

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

        items = (
            db.query(buyer_model.Buyer)
            .filter(current_user.id == buyer_model.Buyer.id)
            .first()
        )
        items = items.orders
        pdf_filename = f"orders_{current_user.id}.pdf"
    pdf_directory = "static/pdf/"
    if not os.path.exists(pdf_directory):
        os.makedirs(pdf_directory)
    pdf_filepath = os.path.join(pdf_directory, pdf_filename)
    file = canvas.Canvas(pdf_filepath, pagesize=letter)

    file.setFont("Helvetica", 12)

    # Title
    y = 770
    file.setFont("Helvetica-Bold", 20)
    file.drawString(220, y, "Activity Report")
    y -= 50
    y = utils.add_user_info(file, current_user, y)

    if pdf_filename[0] == "p":
        utils.add_seller_elem(
            file=file, db=db, items=items, current_user=current_user, y=y
        )

    else:
        utils.add_buyer_elem(file=file, items=items, y=y)

    file.save()
    PDF_BASE_URL = "http://localhost:8000/"
    pdf_url = PDF_BASE_URL + pdf_filepath
    # Return the path to the PDF file
    return JSONResponse(content={"pdf_url": pdf_url})
