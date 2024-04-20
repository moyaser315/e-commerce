# modules
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# our modules
from .person import Person

class User(Person):
    __tablename__ = "users"
    # attributes
    mobile = Column(String)
    
    # relations
    comments = relationship("Comment", back_populates="user")
    sellerUser = relationship("Seller", back_populates="user")
    buyerUser = relationship("Buyer", back_populates="user")
    
    # functions
    def getMobile(self):
        return self.mobile
    
    def setMobile(self, mobile: str):
        self.mobile = mobile
        
    def makeComment(productID: int):    # creates a comment on the given product
        pass
    
    def removeComment(commentID: int):
        pass

