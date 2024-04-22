# modules
from sqlalchemy import Column, Integer, ForeignKey, Float, CheckConstraint, Date, func
from sqlalchemy.orm import relationship, Session
# our modules
from ..database import Base

class Order(Base):
    __tablename__ = "orders"
    # attributes
    __id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __orderDate = Column(Date, nullable=False, default=func.current_date(), name="orderDate")
    __totalCost = Column(Float, nullable= False, name="totalCost")
    __buyerID = Column(Integer, ForeignKey("buyers.id"), nullable=False, name="buyerID")
    
    # options
    __table_args__ = (
        CheckConstraint('totalCost >= 1', name='min_total_cost'),
    )
    
    # relations
    __orderItems = relationship("OrderItem", backref="__order")
    __buyer = relationship("Buyer", backref="__orders")
    
    # properties
    @property
    def id(self):
        return self.__id
    
    @property
    def orderItems(self):
        return self.__orderItems
    
    @property
    def totalCost(self):
        return self.__totalCost
    
    @totalCost.setter
    def totalCost(self, value: float):
        if (value < 1):
            raise Exception("Total Price can't be smaller than 1")
        
        if (self.totalCost):
            raise Exception("Can't override total cost")
        
        self.__totalCost = value
    
    @property
    def orderDate(self):
        return self.__orderDate
    
    @property
    def buyer(self):
        return self.__buyer
    
    @property
    def buyerID(self):
        return self.__buyerID
    
    @buyerID.setter
    def buyerID(self, value: int):
        if (value < 0):
            raise Exception("Invalid buyer id")
        
        if (self.buyerID):
            raise Exception("Can't override current buyer id")
        
        self.__buyerID = value
    
    # functions
    def getOrderItem(self, productID: int, db: Session):
        pass
    
    def addOrderItem(self, productID: int, quantity: int, db: Session):
        pass
    
    