from alembic import op
from sqlalchemy import Column, String, Integer

def upgrade():
    """Create the 'courses' table with 'name' and 'level' columns."""
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )

def downgrade():
    """Drop the 'courses' table."""
    op.drop_table('courses')