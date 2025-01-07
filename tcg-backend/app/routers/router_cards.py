from fastapi import APIRouter
import repository.cards as cards
from schemas.cards import CardDetail, CardImage
from dependencies.base import get_generic_session
from repository.session import SessionDAL
from fastapi import Depends
from typing import List
from pydantic import NonNegativeInt, PositiveInt

router = APIRouter()

# Devuelve una lista de cartas
# @param skip: int - El número de cartas a omitir
# @param limit: int - El número de cartas a devolver
# @return: List[Card] - Una lista de cartas
@router.get("", response_model=List[CardImage])
def get_sets(
    skip: NonNegativeInt = 0,
    limit: PositiveInt = 100,
    session: SessionDAL = Depends(get_generic_session),
):
    return cards.get_cards(skip, limit, session)

# Obtiene una card por su id
# @param id: str - El id de la card
# @param session: SessionDAL - La sesión de la base de datos
# @return: CardDetail - La card
@router.get("/{id}", response_model=CardDetail)
def get_card_by_id(
    id: str,
    session: SessionDAL = Depends(get_generic_session),
):
    return cards.get_card_by_id(id, session)