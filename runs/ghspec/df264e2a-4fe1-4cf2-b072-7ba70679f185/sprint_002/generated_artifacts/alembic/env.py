```python
# alembic/env.py

import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.models.student import Base  # Importing the Base for the Student model

# This is the Alembic Config object, which provides access to
# the values within the .ini file in use. It is used to configure
# settings and connect to the database.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers based on the specified configuration file
fileConfig(config.config_file_name)

# Add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata  # Set the target_metadata for Alembic

def run_migrations_offline():
    """Run migrations in 'offline' mode.
    
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we can avoid a DBAPI connection.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, dialect_opts={"paramstyle": "named"})

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.
    
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    configuration = config.get_section(config.config_ini_section)
    connectable = engine_from_config(
        configuration,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Ensures to compare column types during autogenerate
        )

        with context.begin_transaction():
            context.run_migrations()

# Determine if we are running migrations offline or online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```