from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session


from ..schemas import person
from .. import utils
from ..models import seller, buyer, user
from ..database import get_db
from .. import oauth


router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=person.GetPerson
)
def create_user(user: person.CreatePerson, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    if user.user_type == "seller":
        new_user = seller.Seller(**user.model_dump())
    else:
        new_user = buyer.Buyer(**user.model_dump())

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email is already used"
        )

    return new_user


@router.get("/{id}", response_model=person.GetPerson)
def get_user(id: int, db: Session = Depends(get_db)):
    usr = db.query(user.User).filter(user.User.id == id).first()
    if not usr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there's no user with id : {id}",
        )

    return usr


@router.delete("")
def delete_user(
    current_user: user.User = Depends(oauth.get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, str]:
    try:
        db.delete(current_user)
        db.commit()
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Couldn't delete user",
        )

    return {"message": "Success"}


#### dev only :
# @router.get("/", response_model=List[person.GetPerson])
# def get_users(db: Session = Depends(get_db)):
#     user = db.query(Person).all()
#     return user
