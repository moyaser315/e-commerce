# modules
from sqlalchemy import Column, String, Integer, ForeignKey, Float, CheckConstraint
from sqlalchemy.orm import relationship
# our modules
from helpers.database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class OrderItem(Base):
    __tablename__ = "orderItems"
    # attributes
    id = Column(Integer, primary_key=True)
    productName = Column(String, nullable= False)
    productPrice = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    productID = Column(Integer, ForeignKey("products.id"))
    orderID = Column(Integer, ForeignKey("orders.id"), nullable=False)
    
    # options
    __table_args__ = (
        CheckConstraint('quantity >= 1', name='min_orderItem_quantity'),
    )
    
    # relations
    product = relationship("Product", back_populates="orderItems")
    order = relationship("Order", back_populates="orderItems")
    
    # functions
    def getProduct(self):
        return self.product
    
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity: int):
        self.quantity = quantity
        
    def getOrder(self):
        return self.order
        
    