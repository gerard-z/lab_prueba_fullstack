from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Definición de la base declarativa para los modelos ORM
Base = declarative_base()

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PORT = os.getenv("DATABASE_PORT")

required_vars = {
    "DATABASE_USER": DATABASE_USER,
    "DATABASE_PASSWORD": DATABASE_PASSWORD,
    "DATABASE_HOST": DATABASE_HOST,
    "DATABASE_NAME": DATABASE_NAME,
    "DATABASE_PORT": DATABASE_PORT,
}

# Comprobar si alguna de ellas es None
for var_name, var_value in required_vars.items():
    if var_value is None or var_value == "":
        raise EnvironmentError(f"La variable de entorno '{var_name}' no está definida.")

# Crea el motor de la base de datos SQLAlchemy
database_url = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
engine = create_engine(database_url, echo=False)


# Configuración de la sesión ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
