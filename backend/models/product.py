# modules
from sqlalchemy import Column, Integer, String, Float, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship, Session
import re
# our modules
from ..database import Base
from .comment import Comment



class Product(Base):
    __tablename__ = "products"
    # attributes
    __id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __name = Column(String, nullable=False, name="name")
    __description = Column(String, nullable=False, name="description")
    __price = Column(Float, nullable=False, name="price")
    __quantity = Column(Integer, nullable=False, name="quantity")
    __imgPath = Column(String, name="imgPath")    # see if you need to set nullable = false
   # __sellerID = Column(Integer, ForeignKey("sellers.id"), nullable=False, name="sellerID")
    
    # options
    __table_args__ = (
        CheckConstraint('price >= 1', name='min_product_price'),
        CheckConstraint('quantity >= 0', name='min_product_quantity'),
    )
    
    # relations
    #__comments = relationship("Comment", backref="__product")
    #__seller = relationship("Seller", backref="__products")
    __orderItems = relationship("OrderItem", backref="__product")
    
    # properties
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str): # check validation later
        value = value.strip()
        if (value is None or value == "" or not re.match(r"^[a-zA-Z]+$", value)):
            raise Exception("Name needs to be at least a character")
        
        self.__name = value
        
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value: str):  # check validation later
        value = value.strip()
        if (value is None or value == "" or not re.match(r"^[a-zA-Z]+$", value)):
            raise Exception("Description needs to be at least a character")
        
        self.__description = value
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value: float):
        if (value < 1):
            raise Exception("Price needs to be at least 1")
        
        self.__price = value
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if (value < 0):
            raise Exception("Quantity can't be smaller than 0")
        
        self.__quantity = value
        
    @property
    def imgPath(self):
        return self.__imgPath
    
    @imgPath.setter
    def imgPath(self, value: str):
        value = value.strip()
        if (value == ""):
            value = None
            
        self.__imgPath = value
        
    @property
    def comments(self):
        return self.__comments
    
    # @property
    # def seller(self):
    #     return self.__seller
    
    # @property
    # def sellerID(self):
    #     return self.__sellerID
    
    # @sellerID.setter
    # def sellerID(self, value: int):
    #     if (value < 0 or value is None):
    #         raise Exception("Invalid seller id")
        
    #     if (self.sellerID):
    #         raise Exception("Can't override current seller")
        
    #     self.__sellerID = value
    
    @property
    def orderItems(self):
        return self.__orderItems
    
    
    # functions
    def addComment(self, text: str, userID: int, db: Session):
        comment = Comment(text = text, productID = self.id, userID = userID)
        db.add(comment)
        db.commit()
        db.refresh(comment)
        
        return comment.id
        
        