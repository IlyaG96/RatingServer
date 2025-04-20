import asyncio
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from testcontainers.postgres import PostgresContainer

from src.infrastructure.database.async_database import SQLAlchemyDataBase
from src.infrastructure.database.models.base import Base  # noqa: F401


@pytest.fixture(scope="function")
async def database(postgres_container_url, apply_migrations):
    """
    Creates an AsyncDatabase instance connected to the container,
    applies Alembic migrations on setup, and downgrades on teardown.
    """
    db = SQLAlchemyDataBase(database_url=postgres_container_url)
    yield db
    await db.close()

@pytest.fixture(scope="session")
async def apply_migrations(postgres_container_url):
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



@pytest.fixture(scope="session")
async def postgres_container_url():
    with PostgresContainer("postgres:16") as postgres:
        db_url = postgres.get_connection_url().replace("psycopg2", "asyncpg")
        yield db_url
