from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy import or_
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.oauth import get_current_user, create_access_token
from backend.models.user import User
from backend.models.buyer import Buyer
from backend.models.seller import Seller
from backend.utils import verify,hash
from backend.schemas.person import CreatePerson


class UserService:
    
    @staticmethod
    def auth_user(sent_user: OAuth2PasswordRequestForm , db: Session):
        user = db.query(User).filter(or_(sent_user.username == User.email, sent_user.username == User.phone)).first()
        
        if not user or  not verify(sent_user.password,user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail = "Invalid Username or Password")
        token = create_access_token(data={"user_id": user.id})
        return token
        
    def create_user(user: CreatePerson, db: Session):
        user.password = hash(user.password)
        if user.user_type == "seller":
            new_user = Seller(**user.model_dump())
        else:
            new_user = Buyer(**user.model_dump())
        
        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        except:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="User is already used or invalid input")
        
        return new_user
    
    @staticmethod
    def verify_user(user :OAuth2PasswordRequestForm = Depends(get_current_user), db = Depends(get_db)):
        pass