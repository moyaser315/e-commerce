# modules
from sqlalchemy import ForeignKey, CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
import re

# our modules
from ..database import Base
from .seller import Seller

# from .comment import Comment


class Product(Base):
    __tablename__ = "products"
    # attributes
    __id: Mapped[int] = mapped_column("id", primary_key=True, autoincrement=True)
    __name: Mapped[str] = mapped_column("name", String(40), nullable=False)
    __description: Mapped[str] = mapped_column(
        "description", String(200), nullable=False
    )
    __price: Mapped[float] = mapped_column("price", nullable=False)
    __quantity: Mapped[int] = mapped_column("quantity", nullable=False)
    __imgPath: Mapped[str] = mapped_column(
        "imgPath", nullable=True
    )  # see if you need to set nullable = false
    __cat: Mapped[str] = mapped_column("cat", nullable=False)
    # relations
    __sellerID: Mapped[int] = mapped_column(
        "sellerID", ForeignKey("sellers.id"), nullable=False
    )
    seller: Mapped[Seller] = relationship(back_populates="products")

    # comments: Mapped[list["Comment"]] = relationship(back_populates="product")
    orderItems: Mapped[list["OrderItem"]] = relationship(back_populates="product")

    # options
    __table_args__ = (  # may throw an error
        CheckConstraint("price >= 1", name="min_product_price"),
        CheckConstraint("quantity >= 0", name="min_product_quantity"),
    )

    # properties
    @hybrid_property
    def id(self):
        return self.__id

    @hybrid_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):  # check validation later
        value = value.strip()
        if value is None or value == "" or not re.match(r"^[a-zA-Z]+$", value):
            raise Exception("Name needs to be at least a character")

        self.__name = value

    @hybrid_property
    def cat(self):
        return self.__cat

    @cat.setter
    def cat(self, value: str):  # check validation later
        value = value.strip()
        if value is None or value == "" or not re.match(r"^[a-zA-Z]+$", value):
            raise Exception("Name needs to be at least a character")

        self.__cat = value

    @hybrid_property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):  # check validation later
        value = value.strip()
        # if (value is None or value == "" or not re.match(r"^[a-zA-Z]+$", value)):
        #     raise Exception("Description needs to be at least a character")

        self.__description = value

    @hybrid_property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value is None or value < 1:
            raise Exception("Price needs to be at least 1")

        self.__price = value

    @hybrid_property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        if value is None or value < 0:
            raise Exception("Quantity can't be smaller than 0")

        self.__quantity = value

    @hybrid_property
    def imgPath(self):
        return self.__imgPath

    @imgPath.setter
    def imgPath(self, value: str):
        value = value.strip()
        if value == "":
            value = None

        self.__imgPath = value

    @hybrid_property
    def sellerID(self):
        return self.__sellerID

    @sellerID.setter
    def sellerID(self, value: int):
        if value is None or value < 0:
            raise Exception("Invalid seller id")

        if self.sellerID:
            raise Exception("Can't override current seller")

        self.__sellerID = value

    # # functions
    # def addComment(self, text: str, userID: int, db: Session):
    #     comment = Comment(text = text, productID = self.id, userID = userID)
    #     db.add(comment)
    #     db.commit()
    #     db.refresh(comment)

    #     return comment.id
