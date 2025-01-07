from sqlalchemy import select, func
from models.set import Set
from models.card import Card
from repository.session import SessionDAL

# Obtiene los sets
# @param skip: int - El número de sets a saltar
# @param limit: int - El número de sets a obtener
# @param session: SessionDAL - La sesión de la base de datos
# @return: list[Set] - Los sets
def get_sets(skip: int, limit: int, session: SessionDAL):
    return session.get_all(select(Set), skip, limit)

# Obtiene el número de cartas de un set
# @param set_id: str - El id del set
# @param session: SessionDAL - La sesión de la base de datos
# @return: int - El número de cartas del set
def get_set_size(set_id: str, session: SessionDAL):
    result = session.get_scalar(select(func.count(Card.id)).select_from(Card).where(Card.set_id == set_id))
    return result