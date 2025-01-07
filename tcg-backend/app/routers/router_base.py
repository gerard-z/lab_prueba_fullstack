from fastapi import APIRouter
from routers import router_sets, router_cards

router = APIRouter()

# Ruta raíz
# @return: dict - Un diccionario con la clave "Hello" y el valor "World"
@router.get("/")
def read_root():
    return {"Hello": "World"}

# Incluye el router de sets
router.include_router(router_sets.router, prefix="/sets", tags=["sets"])

# Incluye el router de cards
router.include_router(router_cards.router, prefix="/cards", tags=["cards"])