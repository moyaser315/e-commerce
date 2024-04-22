# modules
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Relationship, Session
# our modules
from ..database import Base
class SpecializedUser(Base):
    __abstract__ = True
    # attributes
    __id = Column(Integer, ForeignKey("users.id"), primary_key=True, name="id")
    __user: Relationship
    
    # properties
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value: int):
        if (value is None or value < 0):
            raise Exception("Invalid user id")
        
        self.__id = value
    
    
    @property
    def name(self):
        return self.__user.name
    
    @name.setter
    def name(self, value: str):
        self.__user.name = value
        
    @property
    def email(self):
        return self.__user.email
    
    @email.setter
    def email(self, value: str):
        self.__user.email = value
        
    @property
    def mobile(self):
        return self.__user.mobile
    
    @mobile.setter
    def mobile(self, value: str):   # come back and verify
        self.__user.mobile = value

    # functions    
    def login(self, password: str):    # to be implemented
        self.__user.login(password)
    
    def getAllProducts(self, db: Session):   # return all products in the database
        return self.__user.getAllProducts(db)
    
    def getProduct(self, id: int, db: Session):    # return product with the given id
        return self.__user.getProduct(id, db)
        
    def makeComment(self, comment: str, productID: int, db: Session):
        self.__user.makeComment(comment, productID, db)
    
    def removeComment(self, commentID: int, db: Session):
        self.__user.removeComment(commentID, db)