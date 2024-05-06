# modules
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

# our modules
from ..database import Base
from .product import Product
from .user import User


class Comment(Base):
    __tablename__ = "comments"
    # attributes
    __id: Mapped[int] = mapped_column("id", primary_key=True, autoincrement=True)
    __text: Mapped[str] = mapped_column("text", nullable=False)

    # relations
    __productID: Mapped[int] = mapped_column(
        "productID", ForeignKey("products.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    product: Mapped[Product] = relationship(back_populates="comments")

    __userID: Mapped[int] = mapped_column(
        "userID", ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    user: Mapped[User] = relationship(back_populates="comments")

    # properties
    @hybrid_property
    def id(self):
        return self.__id

    @hybrid_property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value: str):
        if value is None or value == "":
            raise Exception("Comment can't be empty")

        self.__text = value

    @hybrid_property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, value: int):
        if value is None or value < 0:
            raise Exception("Invalid user id")

        if self.userID:
            raise Exception("Can't override current user")

        self.__userID = value

    @hybrid_property
    def productID(self):
        return self.__productID

    @productID.setter
    def productID(self, value: int):
        if value is None or value < 0:
            raise Exception("Invalid product id")

        if self.productID:
            raise Exception("Can't override current product")

        self.__productID = value
