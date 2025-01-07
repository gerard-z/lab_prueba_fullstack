from schemas.base import OrmBaseModel
from datetime import datetime

# Esquema de un mercado
class Market(OrmBaseModel):
    id: int
    card_id: str
    url: str
    updated_at: datetime
    market: str