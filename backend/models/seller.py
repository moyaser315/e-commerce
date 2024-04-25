# modules
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
# our modules
from .user import User

class Seller(User):
    __tablename__ = "sellers"
    # attributes
    __id: Mapped[int] = mapped_column("id", ForeignKey("users.id"), primary_key=True)
    __balance: Mapped[float] = mapped_column("balance", nullable=False, default=0)
    
    # relations
    products: Mapped[list["Product"]] = relationship(back_populates="seller", cascade="delete")
    
    # options
    __mapper_args__ = {
        "polymorphic_identity": "seller",
    }
    
    
    # properties
    @hybrid_property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        if (value is None or value < 0):
            raise Exception("Balance can't be smaller than 0")
        
        self.__balance = value
    
    
    # # functions
    # def getSellingProduct(self, id: int, db: Session):
    #     product = db.query(Product).filter(Product.id == id).first()
    #     if not product or (self.id != product.sellerID):
    #         raise Exception("Product doesn't exist")
        
    #     return product
    
    # def sellNewProduct(self, name: str, description: str, price: float, quantity: int, imgPath: str, db: Session):
    #     product = Product(name = name, description = description, price = price, quantity = quantity, imgPath = imgPath, sellerID = self.id)
    #     db.add(product)
    #     db.commit()
    #     db.refresh(product)
        
    #     return product.id
    
    # def updateProduct(self, db: Session, productID: int, **kwargs):
    #     product = db.query(Product).filter(Product.id == productID, Product.sellerID == self.id).first()
    #     if not product:
    #         raise Exception("Product doesn't exist")
        
    #     for attr, value in kwargs.items():
    #         setattr(product, attr, value)
            
    #     db.commit()
    #     return product
    
    # def stopSellingProduct(self, productID: int, db: Session):
    #     product = db.query(Product).filter(Product.id == productID, Product.sellerID == self.id).first()
    #     if not product:
    #         raise Exception("Product doesn't exist")
        
    #     db.delete(product)