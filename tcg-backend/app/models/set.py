from core.database import Base
from models.base import BaseMixin, UpdatedTimeMixin
from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy.orm import relationship

# Modelo de la tabla set
class Set(Base, BaseMixin, UpdatedTimeMixin):
    __tablename__ = "set"
    
    id = Column(String,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    series = Column(String,nullable=False)
    printed_total = Column(Integer)
    total = Column(Integer)
    ptcgo_code = Column(String)
    release_date = Column(DATE)
    symbol_url = Column(String)
    logo_url = Column(String)

    cards = relationship("Card", back_populates="set")