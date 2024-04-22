# modules
from sqlalchemy import Column, Integer, String ,TIMESTAMP
from sqlalchemy.orm import Session
import re

# our modules
from ..database import Base
# from .product import Product

# helpers



class Person(Base):
    __abstract__ = True  # Mark this as an abstract base class
    # # attributes
    # __tablename__ ="person"
    __id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    __name = Column(String, nullable=False, name="name")
    __email = Column(String, unique=True, index=True, nullable=False, name="email")
    __password = Column(String, index=True, nullable=False, name="password")
    __created_at = Column(TIMESTAMP,nullable=False,server_default="NOW()",name="created_at")
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        value = value.strip()
        if (value is None or value == "" or not re.match(r"^[a-zA-Z][a-zA-Z0-9]+$", value)):
            raise Exception("Name needs to start with a character and its length should be 2 or greater")
        
        self.__name = value
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value: str):    # come back and verify
        self.__email = value
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value: str):
        if (bool(re.search(r"\s", value))):
            raise Exception("Password can't have spaces in it")
        
        if (value is None or value == "" or len(value) < 5):
            raise Exception("Password needs to be at least of length 5")
        
        self.__password = value
    @property
    def created_at(self):
        return self.__created_at
        
        
    # # functions
    # def login(self, password: str):    # to be implemented
    #     if (not PWD_CONTEXT.verify(password, self.__password)):
    #         raise Exception("Invalid Password")
        
    #     pass    # login logic should go here
    
    # def getAllProducts(self, db: Session):   # return all products in the database
    #     return db.query(Product).all()
    
    # def getProduct(self, id: int, db: Session):    # return product with the given id
    #     return db.query(Product).filter(Product.id == id).first()
    
    