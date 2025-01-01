from schemas.base import OrmBaseModel
from datetime import date, datetime

class Card(OrmBaseModel):
    id: str
    name: str
    supertype: str
    subtypes: list[str]
    types: list[str]
    set_id: str
    number: str
    rarity: str