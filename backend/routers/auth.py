from fastapi import APIRouter ,Depends,HTTPException ,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models import user as model
from ..database import get_db
from ..schemas.person import Token
from ..utils import verify
from ..oauth import create_access_token


router = APIRouter(prefix='/users/login',tags=["authnication"])

@router.post("/",response_model=Token)
def login(
    user_cerd : OAuth2PasswordRequestForm = Depends() ,
    db : Session = Depends(get_db)
):
    print(user_cerd)
    user = db.query(model.User).filter(model.User.email == user_cerd.username).first()
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

# @router.post("/test",response_model=Token)
# def login(
#     user_cerd : OAuth2PasswordRequestForm = Depends()
# ):
#     return {"access_token": user_cerd.username}