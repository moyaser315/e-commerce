from ..schemas import person
from .. import utils
from ..models.user import User
from fastapi import status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=person.GetPerson)
def create_user(user: person.CreatePerson, db: Session = Depends(get_db)):

    user.password = utils.hash(user.password)
    
    new_user = User(**user.model_dump())
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user





@router.get("/{id}", response_model=person.GetPerson)
def get_user(id: int, db: Session = Depends(get_db)):
    usr = db.query(User).filter(User.id == id).first()
    if not usr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there's no user with id : {id}",
        )
    return 



#### dev only :
# @router.get("/", response_model=List[person.GetPerson])
# def get_users(db: Session = Depends(get_db)):
#     user = db.query(Person).all()
#     return user