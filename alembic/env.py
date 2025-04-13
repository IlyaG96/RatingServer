import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

from configuration import DATABASE_URL
from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.game import GameModel  # noqa
from src.infrastructure.database.models.player import PlayerModel  # noqa
from sqlalchemy.engine.base import Connection

config = context.config
connectable = create_async_engine(DATABASE_URL, echo=True)
target_metadata = Base.metadata


async def run_migrations_online() -> None:
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection: Connection) -> None:  # noqa
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


# Запуск миграций
if context.is_offline_mode():
    raise Exception("Offline mode is not supported with asyncpg")
else:
    asyncio.run(run_migrations_online())
