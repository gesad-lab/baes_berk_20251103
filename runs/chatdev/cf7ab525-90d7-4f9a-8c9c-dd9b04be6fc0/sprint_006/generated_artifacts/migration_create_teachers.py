'''
Migration script to create the teachers table.
'''
from sqlalchemy import Column, String, Integer
from alembic import op
def upgrade():
    op.create_table(
        'teachers',
        Column('id', Integer, primary_key=True, index=True),
        Column('name', String, nullable=False),
        Column('email', String, nullable=False)
    )
def downgrade():
    op.drop_table('teachers')