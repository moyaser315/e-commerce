# modules
from sqlalchemy import Column, Integer, ForeignKey, Float, CheckConstraint, Date, func
from sqlalchemy.orm import relationship
# our modules
from helpers.database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class Order(Base):
    __tablename__ = "orders"
    # attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    orderDate = Column(Date, nullable=False, default=func.current_date())
    totalCost = Column(Float, nullable= False)
    buyerID = Column(Integer, ForeignKey("buyers.id"), nullable=False)
    
    # options
    __table_args__ = (
        CheckConstraint('totalCost >= 1', name='min_total_cost'),
    )
    
    # relations
    orderItems = relationship("OrderItem", back_populates="order")
    buyer = relationship("Buyer", back_populates="orders")
    
    # functions
    def getAllOrderItems(self):
        return self.orderItems
    
    def getOrderItem(self, productID: int):
        pass
    
    def addOrderItem(self, productID: int, quantity: int):
        pass
    
    def getTotalCost(self):
        return self.totalCost
    
    def getOrderDate(self):
        return self.orderDate
    
    def cancel(self):
        pass
    
    def getBuyer(self):
        return self.buyer