# modules
from sqlalchemy import Column, Integer, String, Float, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
# our modules
from .database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class Product(Base):
    __tablename__ = "products"
    # attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    imgPath = Column(String)    # see if you need to set nullable = false
    sellerID = Column(Integer, ForeignKey("sellers.id"), nullable=False)
    
    # options
    __table_args__ = (
        CheckConstraint('price >= 1', name='min_price'),
        CheckConstraint('quantity >= 0', name='min_quantity'),
    )
    
    # relations
    comments = relationship("Comment", back_populates="product")
    seller = relationship("Seller", back_populates="products")
    orderItems = relationship("OrderItem", back_populates="product")
    
    # functions
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setName(self, name: str):
        self.name = name
        
    def getDescription(self):
        return self.description
    
    def setDescription(self, desc: str):
        self.description = desc
        
    def getPrice(self):
        return self.price
    
    def setPrice(self, price: float):
        self.price = price
    
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quant: int):
        self.quantity = quant
        
    def getImagePath(self):
        return self.imgPath
    
    def setImagePath(self, path: str):
        self.imgPath = path
        
    def getComments(self):
        return self.comments
    
    def addComment(self, comment: str, userId: int):
        pass
    
    def getOwner(self):
        return self.seller
    
    def getOrderItems(self):
        return self.orderItems
        