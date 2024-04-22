# modules
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Session
import re
# our modules
from .person import Person
from .product import Product
from .comment import Comment

class User(Person):
    __tablename__ = "users"
    # attributes
    __mobile = Column(String, name="mobile")
    
    # relations
    __comments = relationship("Comment", backref="__user")
    __sellerUser = relationship("Seller", backref="__user")
    __buyerUser = relationship("Buyer", backref="__user")
    
    # properties
    @property
    def mobile(self):
        return self.__mobile
    
    @mobile.setter
    def mobile(self, value: str):   # come back and verify
        value = value.strip()
        if (not re.match(r"^[0-9]+$")):
            raise Exception("Invalid mobile number")
        
        self.__mobile = value
    
    @property
    def comments(self):
        return self.__comments
    
    @property
    def specialized(self):
        if (self.__sellerUser):
            return self.__sellerUser
        else:
            return self.__buyerUser
    
    # functions        
    def makeComment(self, comment: str, productID: int, db: Session):
        product = db.query(Product).filter(Product.id == productID).first()
        if not product:
            raise Exception("Product with the given id doesn't exist")
        
        product.addComment(comment, self.id)
    
    def removeComment(self, commentID: int, db: Session):
        comment = db.query(Comment).filter(Comment.id == commentID).first()
        if not comment:
            raise Exception("Comment with the given id doesn't exist")
        
        if (comment.user.id != self.id):
            raise Exception("You can only remove your comments")
        
        db.delete(comment)

