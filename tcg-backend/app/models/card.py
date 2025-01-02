from core.database import Base
from models.base import BaseMixin
from sqlalchemy import Column, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from models.image import Image
from models.market import Market

class Card(Base, BaseMixin):
    __tablename__ = "card"

    id = Column(String,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    supertype = Column(String,nullable=False)
    subtypes = Column(ARRAY(String))
    types = Column(ARRAY(String))
    set_id = Column(String,ForeignKey("set.id"),nullable=False)
    number = Column(String,nullable=False)
    rarity = Column(String)

    set = relationship("Set", back_populates="cards")
    images = relationship("Image", back_populates="card")
    markets = relationship("Market", back_populates="card")