from sqlalchemy import select
from models.card import Card
from repository.session import SessionDAL

def get_cards_by_set_id(set_id: str, skip: int, limit: int, session: SessionDAL):
    return session.get_all(select(Card).where(Card.set_id == set_id), skip, limit)

def get_card_by_id(id: str, session: SessionDAL):
    return session.get(select(Card).where(Card.id == id))