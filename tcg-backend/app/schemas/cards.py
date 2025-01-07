from schemas.base import OrmBaseModel
from schemas.image import Image
from schemas.market import Market

# Esquema de una card
class Card(OrmBaseModel):
    id: str
    name: str
    supertype: str
    subtypes: list[str]
    types: list[str]
    set_id: str
    number: str
    rarity: str

# Esquema de una card con imágenes
class CardImage(Card):
    images: list[Image]

# Esquema de una card con sus imágenes y mercados
class CardDetail(Card):
    images: list[Image]
    markets: list[Market]

class SetCardCount(OrmBaseModel):
    total: int
    name: str

class CardCount(OrmBaseModel):
    total: int
