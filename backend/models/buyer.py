# modules
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
# our modules
from .user import User
from ..database import Base

class Buyer(User):
    __tablename__ = "buyers"
    # attributes
    __id: Mapped[int] = mapped_column("id", ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    
    # relations
    # orders: Mapped[list["Order"]] = relationship(back_populates="buyer")
    # cartItems: Mapped[list["CartItem"]] = relationship(back_populates="buyer")
    
    #options
    __mapper_args__ = {
        "polymorphic_identity": "buyer",
    }
    
    
    # # functions
    # def getOrder(self, id: int, db: Session):
    #     pass
    
    # def makeOrder(self, db: Session):
    #     pass
    
    # def cancelOrder(self, id: int, db: Session):
    #     pass
    
    # def addToCart(self, productID: int, quantity: int, db: Session):
    #     pass
    
    # def removeFromCart(self, productID: int, quantity: int, db: Session):
    #     pass