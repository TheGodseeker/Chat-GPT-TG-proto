# database
import asyncio

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from .config import SQLALCHEMY_ASYNC_DATABASE_URL

async_engine = create_async_engine(
    SQLALCHEMY_ASYNC_DATABASE_URL, echo=True, future=True
)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False, autoflush=True, future=asyncio.get_event_loop()
    )

    async with async_session() as session:
        yield session


class DeclarativeBaseOverload:
    """Description of class Table
    This class implementing Basic Table configuration for using.
    example:

    from settings.db import Table

    class ModelName(table):
        ...
    """

    @declared_attr
    def __tablename__(self):
        """
        overrided propetry __tablename__ for auto set table of class
        """
        folder_name = self.__module__.split(".")[-2]
        class_name = self.__name__.lower()
        return f"{folder_name}_{class_name}"


Base = declarative_base(cls=DeclarativeBaseOverload)
