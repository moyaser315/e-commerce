# modules
from sqlalchemy import Column, Float
from sqlalchemy.orm import relationship
# our modules
from .database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class Seller(Base):
    __tablename__ = "sellers"
    # attributes
    balance = Column(Float, nullable=False, default=0)
    
    # relations
    products = relationship("Product", back_populates="seller")
    
    # functions
    def getBalance(self):
        return self.balance
    
    def setBalance(self, balance: float):
        self.balance = balance
        
    def getSellingProducts(self):
        return self.products
    
    def getSellingProduct(self, id: int):
        pass
    
    def sellNewProduct(self, name: str, description: str, price: float, quantity: int, imgPath: str):
        pass
    
    def updateProduct(self, **kwargs):
        pass
    
    def stopSellingProduct(self, productID: int):
        pass
        
    