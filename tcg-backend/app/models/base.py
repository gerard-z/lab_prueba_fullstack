from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Enum, Float, Integer, ForeignKey
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declared_attr
from core.database import Base
from sqlalchemy.sql import func


# https://docs.sqlalchemy.org/en/20/orm/extensions/automap.html
class BaseMixin:
    @classmethod
    def __repr__(self):
        # Get all the columns and their values dynamically
        columns = ", ".join(
            [
                f"{column.name}={getattr(self, column.name)}"
                for column in self.__table__.columns
            ]
        )
        return f"<{self.__class__.__name__}({columns})>"

    # Retorna el entity_name de una entidad a partir del nombre de su modelo.
    @classmethod
    def get_entity_name(cls):
        return "".join(
            ["_" + i.lower() if i.isupper() else i for i in cls.__name__]
        ).lstrip("_")

    # Retorna la llave primaria de un modelo.
    @classmethod
    def get_primary_key(cls):
        return inspect(cls).primary_key[0]

    # Retorna el nombre de la llave primaria de un modelo.
    @classmethod
    def get_primary_key_name(cls):
        return str(inspect(cls).primary_key[0].name)

    # Revisa si un modelo hereda de la clase TrackTimeMixin, verificando si tiene el método soft_delete.
    # Retorna True si hereda; False si no.
    @classmethod
    def has_track_time_mixin(cls):
        return getattr(cls, "soft_delete", None) is not None


# Permite registrar la fecha de creación.
class CreatedTimeMixin:
    created_at = Column(DateTime, server_default=func.date_trunc("second", func.now()))


# Permite registrar la fecha de borrado lógico.
class DeletedTimeMixin:
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now(timezone.utc).replace(microsecond=0)


# Permite registrar la fecha de modificación.
class UpdatedTimeMixin:
    updated_at = Column(
        DateTime,
        server_default=func.date_trunc("second", func.now()),
        onupdate=func.date_trunc("second", func.now()),
    )


# https://stackoverflow.com/questions/70457778/save-the-created-by-updated-by-and-deleted-by-information
# Permite registrar la fecha de creación, modificación y borrado lógico.
class TrackTimeMixin(CreatedTimeMixin, DeletedTimeMixin, UpdatedTimeMixin):
    pass

def get_class_by_tablename(tablename):
    for c in Base.registry._class_registry.values():
        if hasattr(c, "__tablename__") and c.__tablename__ == tablename:
            return c


def get_class_by_entity_name(entity_name):
    for c in Base.registry._class_registry.values():
        if hasattr(c, "__tablename__") and c.get_entity_name() == entity_name:
            return c


# Obtiene todos los modelos que tengan image id como llave foránea.
def get_all_classes_with_images():
    return [
        c
        for c in Base.registry._class_registry.values()
        if hasattr(c, "__tablename__") and hasattr(c, "image_id")
    ]
