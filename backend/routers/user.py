from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session


from ..schemas import person
from .. import utils
from ..models import seller , buyer ,user
from ..database import get_db


router = APIRouter(prefix="/users", tags=["users"])



@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=person.GetPerson)
def create_user(user: person.CreatePerson, db: Session = Depends(get_db)):

    user.password = utils.hash(user.password)
    if user.user_type == 'seller':
        new_user = seller.Seller(**user.model_dump())
    else :
        new_user = buyer.Buyer(**user.model_dump())
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user





@router.get("/{id}", response_model=person.GetPerson)
def get_user(id: int, db: Session = Depends(get_db)):
    usr = db.query(user.User).filter(user.User.id == id).first()
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