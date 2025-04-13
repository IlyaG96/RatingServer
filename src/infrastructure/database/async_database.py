from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from configuration import DATABASE_URL


class SQLAlchemyDataBase:
    def __init__(self) -> None:
        self._engine: AsyncEngine = create_async_engine(
            DATABASE_URL,
            echo=True,
            connect_args={"timeout": 2},
            pool_size=20,
            max_overflow=10,
        )
        self._session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Контекстный менеджер для управления сессией и транзакциями."""
        async with self._session_factory() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise

database = SQLAlchemyDataBase()