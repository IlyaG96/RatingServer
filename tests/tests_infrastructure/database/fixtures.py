from pathlib import Path
from typing import Any, AsyncGenerator, Coroutine

import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from testcontainers.postgres import PostgresContainer

from alembic import command
from alembic.config import Config
from src.infrastructure.database.async_database import SQLAlchemyDataBase
from src.infrastructure.database.models.base import Base  # noqa: F401


@pytest.fixture(scope="session")
async def postgres_container_url() -> AsyncGenerator[str, Any]:
    with PostgresContainer("postgres:16") as postgres:
        db_url = postgres.get_connection_url().replace("psycopg2", "asyncpg")
        yield db_url


@pytest.fixture(scope="function")
async def database(postgres_container_url: str, apply_migrations: Coroutine) -> AsyncGenerator[SQLAlchemyDataBase, Any]:
    db = SQLAlchemyDataBase(database_url=postgres_container_url)
    yield db
    await db.close()


@pytest.fixture(scope="session")
async def apply_migrations(postgres_container_url: str) -> AsyncGenerator[None, Any]:
    project_root = Path(__file__).parent.parent.parent.parent
    alembic_cfg = Config(str(project_root / "alembic.ini"))
    alembic_cfg.set_main_option("sqlalchemy.url", postgres_container_url)
    alembic_cfg.set_main_option("script_location", str(project_root / "alembic"))

    migration_engine = create_async_engine(postgres_container_url, poolclass=NullPool)
    async with migration_engine.begin() as conn:
        await conn.run_sync(lambda sync_conn: command.upgrade(alembic_cfg, "head"))

    yield

    async with migration_engine.begin() as conn:
        await conn.run_sync(lambda sync_conn: command.downgrade(alembic_cfg, "base"))

    await migration_engine.dispose()
