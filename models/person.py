# modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# our modules
from .database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class Person(Base):
    __tablename__ = "people"
    __abstract__ = True  # Mark this as an abstract base class
    # attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    
    
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setName(self, name: str):
        self.name = name
        
    def getEmail(self):
        return self.email
    
    def setEmail(self, email: str):
        self.email = email
        
    def login():    # to be implemented
        pass
    
    def getAllProducts():   # return all products in the database
        pass
    
    def getProduct(id: int):    # return product with the given id
        pass
    
    