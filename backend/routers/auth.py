from fastapi import APIRouter ,Depends,HTTPException ,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models.buyer import Buyer
from ..database import get_db
from ..schemas.person import Token
from ..utils import verify
from ..oauth import create_access_token


router = APIRouter(prefix='/login',tags=["authnication"])

@router.post("/",response_model=Token)
def login(
    user_cerd : OAuth2PasswordRequestForm = Depends() ,
    db : Session = Depends(get_db)
):
    user = db.query(Buyer).filter(Buyer.email == user_cerd.username).first()
    if not user :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="invalid cerdintials"
        )
    if not verify(user_cerd.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="invalid cerdintials"
        )
    token = create_access_token({"user_id" : user.id})
    return {"access_token": token, "token_type": "Bearer"}