```python
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

class Student(db.Model):
    """Model representing a student in the database."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New Field

def upgrade():
    """Upgrade the database schema to add the 'email' field to the Student table."""
    with db.engine.connect() as connection:
        # Check if 'email' column already exists
        if not column_exists("students", "email"):
            # Add new column 'email' to the 'students' table
            connection.execute('ALTER TABLE students ADD COLUMN email VARCHAR NOT NULL')

def downgrade():
    """Downgrade the database schema, removing the 'email' field from the Student table."""
    with db.engine.connect() as connection:
        # Remove the 'email' column if exists (Postgres example, adapt as necessary)
        connection.execute('ALTER TABLE students DROP COLUMN email IF EXISTS')

def column_exists(table_name, column_name):
    """Check if a column exists in a given table."""
    return column_name in [c['name'] for c in db.engine.execute(f"PRAGMA table_info({table_name})").fetchall()]
```