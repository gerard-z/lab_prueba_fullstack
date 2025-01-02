from core.database import Base
from models.base import BaseMixin, UpdatedTimeMixin
from sqlalchemy import Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

class Market(Base, BaseMixin, UpdatedTimeMixin):
    __tablename__ = "market"

    id = Column(BigInteger,primary_key=True,nullable=False,autoincrement=True)
    card_id = Column(String,ForeignKey("card.id"),nullable=False)
    url = Column(String,nullable=False)
    market = Column(String,nullable=False)

    card = relationship("Card", back_populates="markets")