# modules
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# our modules
from .user import User


class Admin(User):
    __tablename__ = "admins"
    # attributes
    __id: Mapped[int] = mapped_column("id", ForeignKey("users.id"), primary_key=True)

    # options
    __mapper_args__ = {
        "polymorphic_identity": "admin",
    }

    # properties

    # # functions
    # def removeProduct(self, id: int, db: Session):
    #     pass

    # def deleteUser(self, id: int, db: Session):
    #     pass

    # def deleteComment(self, id: int, db: Session):
    #     pass
