from sqlalchemy import select
from models.set import Set
from repository.session import SessionDAL

def get_sets(skip: int, limit: int, session: SessionDAL):
    return session.get_all(select(Set), skip, limit)
