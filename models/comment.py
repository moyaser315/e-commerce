# modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# our modules
from helpers.database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class Comment(Base):
    __tablename__ = "comments"
    # attributes
    __id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __text = Column(String, nullable=False, name="text")
    __productID = Column(Integer, ForeignKey("products.id"), nullable=False, name="productID")
    __userID = Column(Integer, ForeignKey("users.id"), nullable=False, name="userID")
    
    # relations
    __product = relationship("Product", backref="__comments")
    __user = relationship("User", backref="__comments")
    
    # properties
    @property
    def id(self):
        return self.__id
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, value: str):
        if (value is None or value == ""):
            raise Exception("Comment can't be empty")
        
        self.__text = value
        
    @property
    def user(self):
        return self.__user
    
    @property
    def userID(self):
        return self.__userID
    
    @userID.setter
    def userID(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid user id")
        
        if (self.userID):
            raise Exception("Can't override current user")
        
        self.__userID = value
    
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
        
        if (self.userID):
            raise Exception("Can't override current product")
        
        self.__productID = value