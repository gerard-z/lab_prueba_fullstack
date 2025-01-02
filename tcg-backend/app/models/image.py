from core.database import Base
from models.base import BaseMixin
from sqlalchemy import Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

class Image(Base, BaseMixin):
    __tablename__ = "image"

    id = Column(BigInteger,primary_key=True,nullable=False,autoincrement=True)
    card_id = Column(String,ForeignKey("card.id"),nullable=False)
    url = Column(String,nullable=False)
    type = Column(String,nullable=False)

    card = relationship("Card", back_populates="images")