from fastapi import APIRouter
from routers import router_sets, router_cards

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = ""):
    return {"item_id": item_id, "q": q}

router.include_router(router_sets.router, prefix="/sets", tags=["sets"])
router.include_router(router_cards.router, prefix="/cards", tags=["cards"])