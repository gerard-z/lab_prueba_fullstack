from fastapi import APIRouter, Depends
import repository.sets as sets
from typing import List, Optional, Literal
from pydantic import NonNegativeInt, PositiveInt, TypeAdapter
from schemas.sets import Set
from dependencies.base import get_generic_session
from repository.session import SessionDAL

router = APIRouter()

@router.get("/", response_model=List[Set])
def get_sets(
    skip: NonNegativeInt = 0,
    limit: PositiveInt = 100,
    session: SessionDAL = Depends(get_generic_session),
):
    return sets.get_sets(skip, limit, session)