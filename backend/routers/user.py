from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from backend.schemas import person
from backend.services.users_services import UserService
from backend.models import user
from backend.database import get_db
from backend import oauth


router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=person.GetPerson
)
def create_user(user: person.CreatePerson, db: Session = Depends(get_db)):
    return UserService.create_user(user, db)


@router.post("/login", response_model=person.Token)
def login(
    user_cerd: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    token = UserService.auth_user(user_cerd, db)
    return {"access_token": token, "token_type": "Bearer"}


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
        print(error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Couldn't delete user",
        )

    return {"message": "Success"}
