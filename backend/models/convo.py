from backend.database import Base
from sqlalchemy import Column, Integer

class Convo(Base):
    __tablename__ = 'conversations'
    
    id = Column(Integer, primary_key=True, index = True)
    