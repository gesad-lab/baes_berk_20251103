```python
# migrations/2023_XX_XX_XXXXXX_create_teachers_table.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def upgrade():
    """Create Teacher table in the database."""
    meta = MetaData(bind=engine)
    teachers = Table(
        'teachers',
        meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),  # Name is a required field
        Column('email', String, nullable=False, unique=True),  # Email is unique and required
        UniqueConstraint('email', name='uq_email')  # Unique constraint for email
    )
    # Create the table if it does not exist already
    meta.create_all(engine, checkfirst=True)

def downgrade():
    """Drop the Teacher table if it exists."""
    with engine.connect() as conn:
        conn.execute("DROP TABLE IF EXISTS teachers;")  # Ensure the table is dropped

if __name__ == "__main__":
    upgrade()
```