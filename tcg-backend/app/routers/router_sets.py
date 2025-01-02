from fastapi import APIRouter, Depends
import repository.sets as sets
import repository.cards as cards
from typing import List
from pydantic import NonNegativeInt, PositiveInt
from schemas.sets import Set
from schemas.cards import Card
from dependencies.base import get_generic_session
from repository.session import SessionDAL
from dependencies.sets import check_set_id

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
