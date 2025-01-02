from sqlalchemy import select
from models.card import Card
from repository.session import SessionDAL

# Obtiene las cards de un set
# @param set_id: str - El id del set
# @param skip: int - El número de cards a saltar
# @param limit: int - El número de cards a obtener
# @param session: SessionDAL - La sesión de la base de datos
# @return: list[Card] - Las cards del set
def get_cards_by_set_id(set_id: str, skip: int, limit: int, session: SessionDAL):
    return session.get_all(select(Card).where(Card.set_id == set_id), skip, limit)

# Obtiene una card por su id
# @param id: str - El id de la card
# @param session: SessionDAL - La sesión de la base de datos
# @return: Card - La card
def get_card_by_id(id: str, session: SessionDAL):
    return session.get(select(Card).where(Card.id == id))