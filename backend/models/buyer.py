# modules
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
# our modules
from .specializedUser import SpecializedUser
from ..database import Base
# from .order import Order

class Buyer(SpecializedUser,Base):
    __tablename__ = "buyers"    
    # relations
    __user = relationship("User", backref="__buyerUser")
    # __orders = relationship("Order", backref="__buyer")
    # __cartItems = relationship("CartItem", backref="__buyer")
    
    # functions
    @property
    def id(self):
        return self.__id
    
    # @property
    # def orders(self):
    #     return self.__orders
    
    @property
    def user(self):
        return self.__user
    
    # @property
    # def cartItems(self):
    #     return self.__cartItems
    
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
    