from sqlalchemy import create_engine

from alembic import context
from configuration import DATABASE_URL
from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.game import GameModel  # noqa
from src.infrastructure.database.models.player import PlayerModel  # noqa

config = context.config
database_url = config.get_main_option("sqlalchemy.url", DATABASE_URL)
connectable = create_engine(database_url.replace("postgresql+asyncpg", "postgresql+psycopg2"), echo=True)
target_metadata = Base.metadata


def run_migrations_online() -> None:
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


# Запуск миграций
if context.is_offline_mode():
    raise Exception("Offline mode is not supported")
else:
    run_migrations_online()
