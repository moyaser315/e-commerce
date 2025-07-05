# modules
from sqlalchemy import ForeignKey, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date

# our modules
from ..database import Base
from .buyer import Buyer


class Order(Base):
    __tablename__ = "orders"
    # attributes
    __id: Mapped[int] = mapped_column("id", primary_key=True, autoincrement=True)
    __orderDate: Mapped[date] = mapped_column(
        "orderDate", nullable=False, default=func.current_date()
    )
    __totalCost: Mapped[float] = mapped_column("totalCost", nullable=False)

    # relations
    __buyerID: Mapped[int] = mapped_column(
        "buyerID",
        ForeignKey("buyers.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True,
    )
    buyer: Mapped[Buyer] = relationship(back_populates="orders")
    orderItems: Mapped[list["OrderItem"]] = relationship(
        back_populates="order", cascade="all, delete-orphan"
    )

    # # options
    __table_args__ = (CheckConstraint("totalCost >= 0", name="min_total_cost"),)

    # properties
    @hybrid_property
    def id(self):
        return self.__id

    @hybrid_property
    def totalCost(self):
        return self.__totalCost

    @totalCost.setter
    def totalCost(self, value: float):
        self.__totalCost = value

    @hybrid_property
    def orderDate(self):
        return self.__orderDate

    @hybrid_property
    def buyerID(self):
        return self.__buyerID

    @buyerID.setter
    def buyerID(self, value: int):
        if value < 0:
            raise Exception("Invalid buyer id")

        if self.buyerID:
            raise Exception("Can't override current buyer id")

        self.__buyerID = value

    # # functions
    # def getOrderItem(self, productID: int, db: Session):
    #     pass

    # def addOrderItem(self, productID: int, quantity: int, db: Session):
    #     pass
