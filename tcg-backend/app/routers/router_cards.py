from fastapi import APIRouter
import repository.cards as cards
from schemas.cards import CardDetail
from dependencies.base import get_generic_session
from repository.session import SessionDAL
from fastapi import Depends

router = APIRouter()

@router.get("/{id}", response_model=CardDetail)
def get_card_by_id(
    id: str,
    session: SessionDAL = Depends(get_generic_session),
):
    return cards.get_card_by_id(id, session)