# modules
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Relationship
# our modules
from helpers.database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class SpecializedUser(Base):
    __abstract__ = True
    # attributes
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user: Relationship
    
    # functions
    def getID(self):
        return self.user.getID()
    
    def getName(self):
        return self.user.getName()
    
    def setName(self, name: str):
        self.user.setName(name)
        
    def getEmail(self):
        return self.user.getEmail()
    
    def setEmail(self, email: str):
        self.user.setEmail(email)
        
    def checkValidPassword(self, hashed_pass: str) -> bool:
        return self.user.checkValidPassword(hashed_pass)
        
    def login(self):    # to be implemented
        self.user.login()
    
    def getAllProducts(self):   # return all products in the database
        self.user.getAllProducts()
    
    def getProduct(self, id: int):    # return product with the given id
        self.user.getProduct(id)
    
    def getMobile(self):
        return self.user.getMobile()
    
    def setMobile(self, mobile: str):
        self.user.setMobile(mobile)
        
    def makeComment(self, productID: int):    # creates a comment on the given product
        self.user.makeComment(productID)
    
    def removeComment(self, commentID: int):
        self.user.removeComment(commentID)