from schemas.base import OrmBaseModel
from datetime import date, datetime
from schemas.cards import Card

class Set(OrmBaseModel):
    id: str
    name: str
    series: str
    printed_total: int
    total: int
    ptcgo_code: str
    release_date: date
    updated_at: datetime
    symbol_url: str
    logo_url: str

class SetDetail(Set):
    cards: list[Card]
