from fastapi import APIRouter, Depends
import repository.sets as sets
import repository.cards as cards
from typing import List
from pydantic import NonNegativeInt, PositiveInt
from schemas.sets import Set, SetDetail
from schemas.cards import Card
from dependencies.base import get_generic_session
from repository.session import SessionDAL
from dependencies.sets import check_set_id, get_set_by_id

router = APIRouter()

@router.get("/", response_model=List[Set])
def get_sets(
    skip: NonNegativeInt = 0,
    limit: PositiveInt = 100,
    session: SessionDAL = Depends(get_generic_session),
):
    return sets.get_sets(skip, limit, session)


@router.get("/{set_id}/cards", response_model=List[Card])
def get_cards_by_set_id(
    skip: NonNegativeInt = 0,
    limit: PositiveInt = 100,
    set_id: str = Depends(check_set_id),
    session: SessionDAL = Depends(get_generic_session),
):
    return cards.get_cards_by_set_id(set_id, skip, limit, session)

# Devuelve un set con sus cards
# @param set: Set - Set obtenido de la ruta, a partir de la id
# @return: SetDetail - El set con sus cards
@router.get("/{set_id}", response_model=SetDetail)
def get_set_by_id(
    set: Set = Depends(get_set_by_id),
):
    return set