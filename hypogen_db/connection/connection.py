from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from hypogen_db.connection.settings import CONNECTION_ITEMS

class Connection:
    def __init__(self, username: str = os.getenv("DB_USER"), password: str = os.getenv("DB_PASSWORD")):

        self._user = username
        self._pwd = password

        self._engine = None
        self._session = None
        self._initialize_engine()

    def _initialize_engine(self):
        url = f"postgresql+psycopg2://{self._user}:{self._password}@{self._host}:{self._port}/{self._database}"
        self._engine = create_engine(url)

    def create_session(self):
        if not self._session:
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
            self._session = SessionLocal()
        return self._session

    @property
    def engine(self):
        return self._engine

# Example usage
connection = Connection(user="username", password="password", host="localhost", port=5432, database="mydatabase")
engine = connection.engine
session = connection.create_session()


# class SQLAlchemyConnection():
#     """
#     A connection object for SQLAlchemy-Sqlite Databases.
#     """

#     def __init__(
#         self, conn_path: str = "postgres_conn", session: Session = None, base: Base = None
#     ) -> None:
#         """
#         Initializes a database session (and connection, by relation).

#         Args:
#             conn_path: The path to the desired database.
#             session: The session to continue using if interactions with the database have already commenced.
#             base: The SQLAlchemy base for a pre-established connection.
#         """
#         if not conn_path.startswith(SQLALCHEMY_URL_PREFIX):
#             conn_path = SQLALCHEMY_URL_PREFIX + conn_path

#         super().__init__(conn_path=conn_path)

#         self._engine = create_engine(self._conn_path, echo=False)

#         if session is not None:
#             self._sesson = session
#         else:
#             Session = sessionmaker(
#                 autocommit=False,
#                 autoflush=False,
#                 bind=self._engine,
#                 expire_on_commit=False,
#             )
#             self._session = Session()

#         if base is not None:
#             self._base = base
#         else:
#             self._base = declarative_base()

#     @property
#     def engine(self) -> Engine:
#         """
#         Creates a SQLAlchemy connection.

#         Returns:
#             A connection in the form of an engine object.
#         """
#         return self._engine

#     @property
#     def session(self) -> Session:
#         """
#         Creates a SQLAlchemy session for the given connection object.

#         Returns:
#             A connection in the form of a session object.
#         """
#         return self._session

#     @property
#     def base(self):
#         """
#         Creates a SQLAlchemy Base for the given connection object.

#         Returns:
#             The Base which goes with the database.
#         """
#         return self._base

