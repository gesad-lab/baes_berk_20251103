'''
Migration script to create the students table.
'''
from sqlalchemy import Column, Integer, String
from alembic import op
def upgrade():
    op.create_table(
        'students',
        Column('id', Integer, primary_key=True, index=True),
        Column('name', String, nullable=False),
        Column('email', String, nullable=False)
    )
def downgrade():
    op.drop_table('students')