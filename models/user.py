# modules
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
import re
# our modules
from database import Base


class User(Base):
    __tablename__ = "users"
    # attributes
    __id: Mapped[int] = mapped_column("id", primary_key=True, autoincrement=True)
    __name: Mapped[str] = mapped_column("name", nullable=False)
    __email: Mapped[str] = mapped_column("email", unique=True, index=True, nullable=False)
    __password: Mapped[str] = mapped_column("password", nullable=False)
    __mobile: Mapped[str] = mapped_column("mobile", nullable=True)
    __type: Mapped[str] = mapped_column("type", nullable=False)
    
    # relations
    comments: Mapped[list["Comment"]] = relationship(back_populates="user")
    
    # options
    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": __type,
    }
    
    
    # properties
    @hybrid_property
    def id(self):
        return self.__id
    
    @hybrid_property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        value = value.strip()
        if (value is None or value == "" or not re.match(r"^[a-zA-Z][a-zA-Z0-9]+$", value)):
            raise Exception("Name needs to start with a character and its length should be 2 or greater")
        
        self.__name = value
        
    @hybrid_property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value: str):    # come back and verify
        self.__email = value
        
    @hybrid_property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value: str):
        if (value is None or value == "" or len(value) < 5):
            raise Exception("Password needs to be at least of length 5")
        
        if (bool(re.search(r"\s", value))):
            raise Exception("Password can't have spaces in it")
        
        self.__password = value
        
    @hybrid_property
    def mobile(self):
        return self.__mobile
    
    @mobile.setter
    def mobile(self, value: str):   # come back and verify
        value = value.strip()
        # if (value is None or not re.match(r"^[0-9]+$", value)):
        #     raise Exception("Invalid mobile number")
        
        self.__mobile = value
        
    @hybrid_property
    def type(self):
        return self.__type  


    # functions
    # def login(self, password: str):    # to be implemented
    #     if (not PWD_CONTEXT.verify(password, self.__password)):
    #         raise Exception("Invalid Password")
        
    #     pass    # login logic should go here
    
    # def getAllProducts(self, db: Session):   # return all products in the database
    #     return db.query(Product).all()
    
    # def getProduct(self, id: int, db: Session):    # return product with the given id
    #     return db.query(Product).filter(Product.id == id).first()
    
    # def makeComment(self, comment: str, productID: int, db: Session):
    #     product = db.query(Product).filter(Product.id == productID).first()
    #     if not product:
    #         raise Exception("Product with the given id doesn't exist")
        
    #     product.addComment(comment, self.id)
    
    # def removeComment(self, commentID: int, db: Session):
    #     comment = db.query(Comment).filter(Comment.id == commentID).first()
    #     if not comment:
    #         raise Exception("Comment with the given id doesn't exist")
        
    #     if (comment.user.id != self.id):
    #         raise Exception("You can only remove your comments")
        
    #     db.delete(comment)