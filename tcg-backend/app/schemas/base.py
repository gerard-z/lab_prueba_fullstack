from datetime import datetime
from typing import List
from pydantic import BaseModel

# Esquema base para los modelos de la base de datos
class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True
        json_encoders = {
            # custom output conversion for datetime
            datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")
        }

    # Crea una lista de instancias de un modelo a partir de una lista de tuplas.
    # @param tpls: List[tuple] | tuple - La lista de tuplas o una tupla
    # @return: List[cls] - La lista de instancias del modelo
    @classmethod
    def from_tuples(cls, tpls: List[tuple] | tuple):
        if isinstance(tpls, list):
            return [
                cls(**{k: v for k, v in zip(cls.__fields__.keys(), tpl)})
                for tpl in tpls
            ]
        return cls(**{k: v for k, v in zip(cls.__fields__.keys(), tpls)})


# Crea un diccionario sin llaves con valores nulos a partir de un diccionario.
# @param a_dict: dict - El diccionario a crear
# @return: dict - El diccionario sin llaves con valores nulos
def create_non_empty_dict(a_dict: dict):
    return {key: a_dict[key] for key in a_dict if a_dict[key] is not None}


# Convierte un payload en formato de schema a un diccionario eliminando
# todas las llaves nulas.
# @param payload: BaseModel - El payload a convertir
# @return: dict - El diccionario sin llaves con valores nulos
def payload_to_dict(payload):
    payload = payload.model_dump()
    return create_non_empty_dict(payload)