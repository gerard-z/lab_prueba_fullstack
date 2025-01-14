from fastapi import APIRouter, Query
import repository.cards as cards
from schemas.cards import CardDetail, CardImage, CardCount
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

# Devuelve el número de cartas
# @param session: SessionDAL - La sesión de la base de datos
# @return: int - El número de cartas
@router.get("/size", response_model=CardCount)
def get_card_size(
    session: SessionDAL = Depends(get_generic_session),
):
    total = cards.get_card_size(session)
    return {"total": total}

@router.get("/search", response_model=List[CardImage])
def search_cards_route(
    q: str = Query(..., min_length=1),
    skip: NonNegativeInt = 0,
    limit: PositiveInt = 20,
    session: SessionDAL = Depends(get_generic_session),
):
    return cards.search_cards(q, skip, limit, session)

@router.get("/search/count", response_model=CardCount)
def search_cards_count_route(
    q: str = Query(..., min_length=1),
    session: SessionDAL = Depends(get_generic_session),
):
    total = cards.search_cards_count(q, session)
    return {"total": total}

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