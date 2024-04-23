# modules
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
# our modules
from database import Base
from .product import Product
from .buyer import Buyer


class CartItem(Base):
    __tablename__ = "cartItems"
    # attributes
    __quantity: Mapped[int] = mapped_column("quantity", nullable=False)
    
    # relations
    __productID: Mapped[int] = mapped_column("productID", ForeignKey("products.id"), primary_key=True)
    product: Mapped[Product] = relationship("Product")
    
    __buyerID: Mapped[int] = mapped_column("buyerID", ForeignKey("buyers.id"), nullable=True, primary_key=True)
    buyer: Mapped[Buyer] = relationship("Buyer", back_populates="cartItems")
    
    # options
    __table_args__ = (
        CheckConstraint('quantity >= 1', name='min_cartItem_quantity'),
    )
    
    
    # properties   
    @hybrid_property
    def productID(self):
        return self.__productID
    
    @productID.setter
    def productID(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid product id")
        
        if (self.productID):
            raise Exception("Can't override product user")
        
        self.__productID = value
    
    @hybrid_property
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