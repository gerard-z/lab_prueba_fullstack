from schemas.base import OrmBaseModel

class Image(OrmBaseModel):
    id: int
    card_id: str
    url: str
    type: str
