# modules
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
# our modules
from .user import User

class Buyer(User):
    __tablename__ = "buyers"
    
    