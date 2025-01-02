from fastapi import Depends, HTTPException
from repository.session import SessionDAL
from dependencies.base import get_model_instance_by_id, get_generic_session
from models.set import Set

# Revisa que la id entregada en la ruta sea un set existente
def check_set_id(set_id: str, session: SessionDAL = Depends(get_generic_session)):
    set = get_model_instance_by_id(Set, set_id, session)
    if not set:
        raise HTTPException(status_code=404, detail="Set not found")
    return set_id

