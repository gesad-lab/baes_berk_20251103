from sqlalchemy import Column, String, Integer
from alembic import op

def upgrade():
    # Create the 'courses' table with columns 'id', 'name', and 'level'
    op.create_table(
        'courses',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )

def downgrade():
    # Drop the 'courses' table if it exists
    op.drop_table('courses')