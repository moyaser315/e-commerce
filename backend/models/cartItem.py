# modules
from sqlalchemy import Column, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
# our modules
from ..database import Base

class CartItem(Base):
    __tablename__ = "cartItems"
    # attributes
    __productID = Column(Integer, ForeignKey("products.id"), primary_key=True, name="productID")
    __buyerID = Column(Integer, ForeignKey("buyers.id"), nullable=True, name="buyerID")
    __quantity = Column(Integer, nullable=False, name="quantity")
    
    
    # options
    __table_args__ = (
        CheckConstraint('quantity >= 1', name='min_cartItem_quantity'),
    )
    
    # relations
    __product = relationship("Product")
    __buyer = relationship("Buyer", backref="__cartItems")
    
    # properties
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
            raise Exception("Can't override product user")
        
        self.__productID = value
        
    @property
    def buyer(self):
        return self.__buyer
    
    @property
    def buyerID(self):
        return self.__buyerID
    
    @buyerID.setter
    def buyerID(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid buyer id")
        
        if (self.buyerID):
            raise Exception("Can't override buyer user")
        
        self.__buyerID = value
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if (value is None or value < 1):
            raise Exception("Quantity must be greater than 1")
            
        self.__quantity = value