# modules
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
# our modules
from .specializedUser import SpecializedUser

class Buyer(SpecializedUser):
    __tablename__ = "buyers"
    # attributes
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    
    # relations
    user = relationship("User", back_populates="buyerUser")
    orders = relationship("Order", back_populates="buyer")
    cartItems = relationship("CartItem", back_populates="buyer")
    
    # functions
    def getAllOrders(self):
        return self.orders
    
    def getOrder(self, id: int):
        pass
    
    def makeOrder(self):
        pass
    
    def cancelOrder(self, id: int):
        pass
    
    def addToCart(self, productID: int, quantity: int):
        pass
    
    def removeFromCart(self, productID: int, quantity: int):
        pass
    