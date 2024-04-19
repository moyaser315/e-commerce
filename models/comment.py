# modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# our modules
from .database import DatabaseHandler

# helpers
Base = DatabaseHandler.getBase()

class Comment(Base):
    __tablename__ = "comments"
    # attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    productID = Column(Integer, ForeignKey("products.id"), nullable=False)
    userID = Column(Integer, ForeignKey("users.id"), nullable=False)
    # relations
    product = relationship("Product", back_populates="comments")
    user = relationship("User", back_populates="comments")
    # functions
    def updateComment(self, txt: str):
        self.text = txt
        
    def deleteComment(self):
        pass
    
    def getOwner(self):
        return self.user
    
    def getProduct(self):
        return self.product