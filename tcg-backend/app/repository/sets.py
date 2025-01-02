from sqlalchemy import select
from models.set import Set
from repository.session import SessionDAL

# Obtiene los sets
# @param skip: int - El número de sets a saltar
# @param limit: int - El número de sets a obtener
# @param session: SessionDAL - La sesión de la base de datos
# @return: list[Set] - Los sets
def get_sets(skip: int, limit: int, session: SessionDAL):
    return session.get_all(select(Set), skip, limit)