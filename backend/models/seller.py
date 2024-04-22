# modules
from sqlalchemy import Column, Float
from sqlalchemy.orm import relationship, Session
# our modules
from .specializedUser import SpecializedUser
from .product import Product

class Seller(SpecializedUser):
    __tablename__ = "sellers"
    # attributes
    __balance = Column(Float, nullable=False, default=0, name="balance")
    
    # relations
    __products = relationship("Product", backref="__seller")
    __user = relationship("User", backref="__sellerUser")
    
    # properties
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        if (value < 0):
            raise Exception("Balance can't be smaller than 0")
        
        self.__balance = value
        
    @property
    def products(self):
        return self.__products
    
    # functions
    def getSellingProduct(self, id: int, db: Session):
        product = db.query(Product).filter(Product.id == id).first()
        if not product or (self.id != product.sellerID):
            raise Exception("Product doesn't exist")
        
        return product
    
    def sellNewProduct(self, name: str, description: str, price: float, quantity: int, imgPath: str, db: Session):
        product = Product(name = name, description = description, price = price, quantity = quantity, imgPath = imgPath, sellerID = self.id)
        db.add(product)
        db.commit()
        db.refresh(product)
        
        return product.id
    
    def updateProduct(self, db: Session, productID: int, **kwargs):
        product = db.query(Product).filter(Product.id == productID, Product.sellerID == self.id).first()
        if not product:
            raise Exception("Product doesn't exist")
        
        for attr, value in kwargs.items():
            setattr(product, attr, value)
            
        db.commit()
        return product
    
    def stopSellingProduct(self, productID: int, db: Session):
        product = db.query(Product).filter(Product.id == productID, Product.sellerID == self.id).first()
        if not product:
            raise Exception("Product doesn't exist")
        
        db.delete(product)
        
    