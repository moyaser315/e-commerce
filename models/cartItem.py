# modules
from sqlalchemy import Column, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
# our modules
from helpers.database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class CartItem(Base):
    __tablename__ = "cartItems"
    # attributes
    productID = Column(Integer, ForeignKey("products.id"), primary_key=True)
    buyerID = Column(Integer, ForeignKey("buyers.id"), nullable=True)
    quantity = Column(Integer, nullable=False)
    
    
    # options
    __table_args__ = (
        CheckConstraint('quantity >= 1', name='min_cartItem_quantity'),
    )
    
    # relations
    product = relationship("Product")
    buyer = relationship("Buyer", back_populates="cartItems")
    
    # functions
    def getProduct(self):
        return self.product
    
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity: int):
        self.quantity = quantity
        
    def getBuyer(self):
        return self.buyer