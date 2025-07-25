from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas import product as schema
from backend.models import user as user_model
from backend import oauth
from backend.services.generate_report import ReportService


router = APIRouter(prefix="/report", tags=["dealing with reports"])

@router.get("/")
async def get_products(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(oauth.get_current_user),
):
    current_user = schema.GetPerson.model_validate(current_user)
    pdf_url = ReportService.generate(current_user,db)
    return JSONResponse(content={"pdf_url": pdf_url})
