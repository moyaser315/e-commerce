# modules
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
# our modules
from database import Base
from .product import Product


class OrderItem(Base):
    __tablename__ = "orderItems"
    # attributes
    __id: Mapped[int] = mapped_column("id", primary_key=True)
    __quantity: Mapped[int] = mapped_column("quantity", nullable=False)
    __buyPrice: Mapped[float] = mapped_column("buyPrice", nullable=False)
    
    # relations
    __productID: Mapped[int] = mapped_column("productID", ForeignKey("products.id"))
    product: Mapped[Product] = relationship("Product", back_populates="orderItems")
    
    __orderID: Mapped[int] = mapped_column("orderID", ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="orderItems")
    
    # options
    __table_args__ = (
        CheckConstraint('quantity >= 1', name='min_orderItem_quantity'),
    )
    
    
    # properties
    @hybrid_property
    def id(self):
        return self.__id
    
    @hybrid_property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if (value is None or value < 1):
            raise Exception("Quantity can't be smaller than 1")
        
        if (self.quantity):
            raise Exception("Can't override current quantity")
        
        self.__quantity = value
        
    @hybrid_property
    def buyPrice(self):
        return self.__buyPrice
    
    @buyPrice.setter
    def buyPrice(self, value: int):
        if (value is None or value < 1):
            raise Exception("Buy Price can't be smaller than 1")
        
        if (self.buyPrice):
            raise Exception("Can't override current buy price")
        
        self.__buyPrice = value
    
    @hybrid_property
    def productID(self):
        return self.__productID
    
    @productID.setter
    def productID(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid product id")
        
        if (self.productID):
            raise Exception("Can't override product id")
        
        self.__productID = value
        
    @hybrid_property
    def orderID(self):
        return self.__orderID
    
    @orderID.setter
    def orderID(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid order id")
        
        if (self.orderID):
            raise Exception("Can't override order id")
        
        self.__orderID = value