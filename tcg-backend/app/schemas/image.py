from schemas.base import OrmBaseModel

# Esquema de una imagen
class Image(OrmBaseModel):
    id: int
    card_id: str
    url: str
    type: str
