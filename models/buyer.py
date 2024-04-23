# modules
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
# our modules
from .user import User


class Buyer(User):
    __tablename__ = "buyers"
    # attributes
    __id: Mapped[int] = mapped_column("id", ForeignKey("users.id"), primary_key=True)
    
    # relations
    orders = relationship("Order", back_populates="buyer")
    cartItems = relationship("CartItem", back_populates="buyer")
    
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