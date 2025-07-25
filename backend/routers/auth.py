from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.schemas.person import Token
from backend.services.users_services import UserService

router = APIRouter(prefix="/users/login", tags=["authnication"])

@router.post("", response_model=Token)
def login(
    user_cerd: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    
    token = UserService.auth_user(user_cerd,db)
    return {"access_token": token, "token_type": "Bearer"}

