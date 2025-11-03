```python
import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from src.db import DATABASE_URL, Base  # Importing the Base metadata for models

# This is the Alembic configuration object
config = context.config

# Set the database URL to the Alembic config from the environment variable
config.set_main_option('sqlalchemy.url', DATABASE_URL)

# Add your model's MetaData object here
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option('sqlalchemy.url')
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Enable comparison of types in migrations
        )

        with context.begin_transaction():
            context.run_migrations()

# Determine whether to run migrations offline or online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```