# modules
from sqlalchemy import Column, String, Integer, ForeignKey, Float, CheckConstraint
from sqlalchemy.orm import relationship
# our modules
from ..database import Base

class OrderItem(Base):
    __tablename__ = "orderItems"
    # attributes
    __id = Column(Integer, primary_key=True, name="id")
    __productName = Column(String, nullable= False, name="productName")
    __productPrice = Column(Float, nullable=False, name="productPrice")
    __quantity = Column(Integer, nullable=False, default=1, name="quantity")
    __productID = Column(Integer, ForeignKey("products.id"), name="productID")
    __orderID = Column(Integer, ForeignKey("orders.id"), nullable=False, name="orderID")
    
    # options
    __table_args__ = (
        CheckConstraint('quantity >= 1', name='min_orderItem_quantity'),
    )
    
    # relations
    __product = relationship("Product", backref="__orderItems")
    __order = relationship("Order", backref="__orderItems")
    
    # functions
    @property
    def productName(self):
        return self.__productName
    
    @productName.setter
    def productName(self, value: str):
        value = value.strip()
        if (value is None or value == ""):
            raise Exception("Product Name can't be empty")
        
        if (self.productName):
            raise Exception("Can't override product name")
        
        self.__productName = value
    
    @property
    def productPrice(self):
        return self.__productPrice
    
    @productPrice.setter
    def productPrice(self, value: float):
        if (value < 1):
            raise Exception("Product price can't be smaller than 1")
        
        if (self.productPrice):
            raise Exception("Can't override product price")
        
        self.__productPrice = value
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if (value < 1):
            raise Exception("Quantity can't be smaller than 1")
        
        if (self.quantity):
            raise Exception("Can't override current quantity")
        
        self.__quantity = value
    
    @property
    def product(self):
        return self.__product
    
    @property
    def productID(self):
        return self.__productID
    
    @productID.setter
    def productID(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid product id")
        
        if (self.productID):
            raise Exception("Can't override product id")
        
        self.__productID = value
        
    @property
    def order(self):
        return self.__order
        
    @property
    def orderID(self):
        return self.__orderID
    
    @orderID.setter
    def orderID(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid order id")
        
        if (self.orderID):
            raise Exception("Can't override order id")
        
        self.__orderID = value
        
    