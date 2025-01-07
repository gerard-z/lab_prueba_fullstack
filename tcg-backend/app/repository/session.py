from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.sql.annotation import AnnotatedAlias
from models.base import BaseMixin, get_class_by_tablename


# DAL: Data Access Layer
# Clase encargada de facilitar las queries a la sesión de la base de datos
class SessionDAL:
    def __init__(self, db: Session):
        self.db = db

    # Obtiene el resultado de ejecutar una select_query sin preocuparse de scalars.
    # COUNTER 0 NO SE SELECIONAN COLUMNAS ESPECIFICAS
    # COUNTER EXISTE, SI SE SELECCIONAN
    # @param select_query: Select - La query a ejecutar
    # @param counter: int - El contador de columnas seleccionadas
    # @return: Result - El resultado de la query
    def get_select_result(self, select_query, counter):
        result = self.db.execute(select_query)
        if not counter:
            result = result.scalars()
        return result

    # Obtiene el resultado de ejecutar una select_query cuando son varios modelos.
    # @param select_query: Select - La query a ejecutar
    # @return: Result - El resultado de la query
    def get_select_result_multiple_models(self, select_query):
        result = self.db.execute(select_query)
        return result.all()

    # Agrega las condiciones base que debe tener cualquier select_query.
    # Retorna la select query con las condiciones base más un contador de cuántas veces se selecionaron
    # campos específicos de un modelo dentro de una select_query.
    # @param select_query: Select - La query a ejecutar
    # @param include_soft_deleted: bool - Si se deben incluir las cards eliminadas lógicamente
    # @return: tuple - La select query con las condiciones base más un contador de cuántas veces se selecionaron
    # campos específicos de un modelo dentro de una select_query
    def __add_select_base_conditions(self, select_query, include_soft_deleted=False):
        models = set()
        for item in select_query._setup_joins:
            # Caso Annotaded Alias
            if isinstance(item[0], AnnotatedAlias):
                tuple_items = list(item)
                for tuple_item in tuple_items:
                    if isinstance(tuple_item, AnnotatedAlias):
                        models.add(get_class_by_tablename(str(tuple_item.element)))
            # Caso normal
            else:
                models.add(get_class_by_tablename(str(item[0])))

        counter = 0
        for item in select_query._raw_columns:
            tablename = str(item).split(".")
            if len(tablename) > 1:
                counter += 1
            table = get_class_by_tablename(tablename[0])
            if table:
                models.add(table)

        if counter and counter < len(select_query._raw_columns):
            raise ValueError(
                "You can only select a list of entire models or model fields, not both."
            )

        for model in models:
            if model and model.has_track_time_mixin() and not include_soft_deleted:
                select_query = select_query.where(model.deleted_at.is_(None))

        return select_query, counter

    # Obtiene una instancia de un modelo o más modelos a partir de una query.
    # @param select_query: Select - La query a ejecutar
    # @param include_soft_deleted: bool - Si se deben incluir las cards eliminadas lógicamente
    # @return: Result - El resultado de la query
    def get(self, select_query, include_soft_deleted=False):
        select_query, counter = self.__add_select_base_conditions(
            select_query=select_query, include_soft_deleted=include_soft_deleted
        )
        result = self.get_select_result(select_query, counter)
        return result.first()

    # Obtiene una instancia de un modelo o más modelos a partir de una query, un modelo específico y su id.
    # @param select_query: Select - La query a ejecutar
    # @param select_model: BaseMixin - El modelo a seleccionar
    # @param id: str - El id del modelo
    # @return: Result - El resultado de la query
    def get_by_id(self, select_query, select_model: BaseMixin, id):
        select_query = select_query.where(select_model.get_primary_key() == id)
        return self.get(select_query)

    # Obtiene un conjunto de instancias de un modelo o más modelos a partir de una query,
    # un offset skip y un límite limit.
    # @param select_query: Select - La query a ejecutar
    # @param skip: int - El número de cards a saltar
    # @param limit: int - El número de cards a obtener
    # @param include_soft_deleted: bool - Si se deben incluir las cards eliminadas lógicamente
    # @param multiple_models: bool - Si se deben obtener varios modelos
    # @return: Result - El resultado de la query
    def get_all(
        self,
        select_query,
        skip=None,
        limit=None,
        include_soft_deleted=False,
        multiple_models=False,
    ):
        select_query, counter = self.__add_select_base_conditions(
            select_query=select_query, include_soft_deleted=include_soft_deleted
        )
        if skip:
            select_query = select_query.offset(skip)
        if limit:
            select_query = select_query.limit(limit)
        if multiple_models:
            result = self.get_select_result_multiple_models(select_query)
            return result
        else:
            result = self.get_select_result(select_query, counter)
            return result.all()

    # Crea una instancia de un modelo particular a partir de un creation_dict (generalmente de un schema)
    # y lo agrega a la base de datos.
    # @param model: BaseMixin - El modelo a crear
    # @param creation_dict: dict - El diccionario de creación
    # @param commit: bool - Si se debe hacer commit
    # @param flush: bool - Si se debe hacer flush
    # @return: Result - El resultado de la query
    def create(self, model: BaseMixin, creation_dict: dict, commit=True, flush=True):
        model_instance = model(**creation_dict)
        try:
            self.db.add(model_instance)
            if commit:
                self.db.commit()
            elif flush:
                self.db.flush()
            if commit or flush:
                self.db.refresh(model_instance)
        except Exception:
            self.db.rollback()
            raise
        return model_instance

    # Actualiza una instancia de un modelo obtenido de la base de datos con datos
    # de un update_dict (generalmente obtenido de un schema). CUIDADO con permitir
    # update_dicts con valores nulos
    # @param model_instance: BaseMixin - El modelo a actualizar
    # @param update_dict: dict - El diccionario de actualización
    # @param commit: bool - Si se debe hacer commit
    # @return: Result - El resultado de la query
    def update(self, model_instance, update_dict: dict, commit=True):
        for key in update_dict:
            setattr(model_instance, key, update_dict[key])
        if commit:
            try:
                # self.db.add(model_instance)
                self.db.commit()
            except:
                self.db.rollback()
                raise
        return model_instance

    # Actualiza una instancia de un modelo obtenido de la base de datos con datos
    # de un update_dict (generalmente obtenido de un schema). CUIDADO con permitir
    # update_dicts con valores nulos
    # @param update_query: Select - La query a ejecutar
    # @param commit: bool - Si se debe hacer commit
    # @return: Result - El resultado de la query
    def update_from_query(self, update_query, commit=True):
        model = get_class_by_tablename(str(update_query.table))
        if model and model.has_track_time_mixin():
            update_query = update_query.where(model.deleted_at.is_(None))
        try:
            self.db.execute(update_query)
            if commit:
                self.db.commit()
        except:
            self.db.rollback()
            raise

    def refresh(self, model_instance):
        self.db.refresh(model_instance)

    # Borra una instancia de un modelo obtenido de la base de datos.
    # @param model_instance: BaseMixin - El modelo a borrar
    # @param hard: bool - Si se debe hacer hard delete
    # @param commit: bool - Si se debe hacer commit
    # @return: Result - El resultado de la query
    def delete(self, model_instance, hard=False, commit=True):
        if model_instance.has_track_time_mixin() and not hard:
            model_instance.soft_delete()
        else:
            self.db.delete(model_instance)
        if commit:
            try:
                self.db.commit()
            except:
                self.db.rollback()
                raise
        return True

    # Borra una instancia de un modelo obtenido de la base de datos a partir de una query.
    # @param delete_query: Select - La query a ejecutar
    # @param commit: bool - Si se debe hacer commit
    # @return: Result - El resultado de la query
    def delete_from_query(self, delete_query, commit=True):
        model = get_class_by_tablename(str(delete_query.table))
        if model and model.has_track_time_mixin():
            delete_query = delete_query.where(model.deleted_at.is_(None))
        try:
            self.db.execute(delete_query)
            if commit:
                self.db.commit()
        except:
            self.db.rollback()
            raise
        return True

    # Realiza un commit en la base de datos.
    # @return: None - Entrega un error si no se puede hacer commit
    def commit(self):
        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    # Cierra la sesión de la base de datos.
    # @return: None - Entrega un error si no se puede cerrar la sesión
    def close(self):
        self.db.close()

    def get_scalar(self, statement):
        result = self.db.execute(statement).scalar()
        return result
