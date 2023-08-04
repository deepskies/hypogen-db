from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_URL_PREFIX = "postgres:///"

Base = declarative_base()


def initialize_database(postgres_path: str) -> Engine:
    """
    Initializes the database at the desired location, generating an engine and session with the autocommit and autoflush
    settings turned off.

    Args:
        postgres_path: The path where the PostgreSQL database should be initialized.

    Returns:
        An engine that connects to the initialized database.
    """
    if not postgres_path.startswith(SQLALCHEMY_URL_PREFIX):
        postgres_path = SQLALCHEMY_URL_PREFIX + postgres_path

    engine = create_engine(postgres_path, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)

    return engine