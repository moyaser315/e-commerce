from sqlalchemy.orm import Session
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from backend.models.seller import Seller
from backend.models.buyer import Buyer
from backend.schemas.person import GetPerson
from backend import utils


import os


class ReportService:
    @staticmethod
    def generate(current_user: GetPerson, db: Session):
        pdf_filename = None
        items = None
        if current_user.user_type.lower() == "seller":
            items = db.query(Seller).filter(current_user.id == Seller.id).first()
            items = items.products
            pdf_filename = f"products_{current_user.id}.pdf"
        else:

            items = db.query(Buyer).filter(current_user.id == Buyer.id).first()
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
        return pdf_url
