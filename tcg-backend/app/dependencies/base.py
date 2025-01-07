from sqlalchemy.future import select
from fastapi import status, HTTPException
from models.base import BaseMixin
from repository.session import SessionDAL
from schemas.base import OrmBaseModel
from fastapi import Depends
from core.database import SessionLocal

# Obtiene una instancia de un modelo a partir de una función que obtiene el modelo
# y una session.
# @param get_function: function - La función que obtiene el modelo
# @param args: tuple - Los argumentos de la función
# @param session: SessionDAL - La sesión de la base de datos
# @return: BaseMixin - La instancia del modelo o una excepción
def get_model_instance(get_function, *args, session: SessionDAL):
    model_instance = None
    flag = False
    for val in args:
        if val:
            flag = True
            break
    if flag:
        model_instance = get_function(*args, session)
        if not model_instance:
            raise HTTPException(
                detail="Object does not exist", status_code=status.HTTP_404_NOT_FOUND
            )

    return model_instance


# Obtiene una instancia de un modelo a partir del nombre del modelo, y la llave primaria
# y una session.
# @param model: BaseMixin - El modelo
# @param primary_key_val: str - La llave primaria
# @param session: SessionDAL - La sesión de la base de datos
# @return: BaseMixin - La instancia del modelo o una excepción
def get_model_instance_by_id(model: BaseMixin, primary_key_val, session: SessionDAL):
    def get_function(id, session: SessionDAL):
        return session.get_by_id(select(model), model, id)

    return get_model_instance(get_function, primary_key_val, session=session)


# Obtiene una instancia de un modelo a partir de un formulario y una session.
# @param model: BaseMixin - El modelo
# @param model_form: OrmBaseModel - El formulario
# @param session: SessionDAL - La sesión de la base de datos
# @param primary_key_name: str - El nombre de la llave primaria
# @return: BaseMixin - La instancia del modelo o una excepción
def get_model_instance_by_id_in_form(
    model: BaseMixin, model_form: OrmBaseModel, session: SessionDAL, primary_key_name
):
    primary_key_val = model_form.model_dump().get(primary_key_name)
    return get_model_instance_by_id(model, primary_key_val, session)


# Verifica una condición y devuelve una excepción si no se cumple
# @param verification_function: function - La función que verifica la condición
# @param fargs: tuple - Los argumentos de la función
# @param status_code: int - El código de estado de la excepción
# @param detail: str - El detalle de la excepción
# @return: None - Si la condición se cumple, o una excepción si no se cumple
def verify_condition(
    verification_function,
    *fargs,
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Bad request",
):
    if not verification_function(*fargs):
        raise HTTPException(status_code=status_code, detail=detail)
    

# Obtiene una session genérica sin requisitos ni User asociado.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtiene una session genérica sin requisitos ni User asociado.
# @param db: SessionDAL - La sesión de la base de datos en el ORM
# @return: SessionDAL - La sesión de la base de datos bajo la DAL
def get_generic_session(db=Depends(get_db)):
    session = SessionDAL(db)
    yield session