from alembic import op
from sqlalchemy import Column, String, Integer

def upgrade():
    """Create the teachers table in the database."""
    op.create_table(
        'teachers',
        Column('id', Integer, primary_key=True),  # Unique identifier for each Teacher
        Column('name', String, nullable=False),    # Teacher's name, cannot be null
        Column('email', String, nullable=False, unique=True)  # Teacher's email, must be unique and cannot be null
    )

def downgrade():
    """Drop the teachers table from the database."""
    op.drop_table('teachers')