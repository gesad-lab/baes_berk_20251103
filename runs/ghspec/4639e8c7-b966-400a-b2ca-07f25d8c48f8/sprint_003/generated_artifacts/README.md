```python
# src/db.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import op
import sqlalchemy as sa

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

def create_database(engine_url: str):
    """Create the initial database and tables if they do not exist."""
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)

def upgrade():
    """Upgrade the database to the new revision by adding the courses table."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    """Downgrade the database by removing the courses table."""
    op.drop_table('courses')

```