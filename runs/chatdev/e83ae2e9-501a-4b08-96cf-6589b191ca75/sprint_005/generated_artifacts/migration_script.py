'''
Migration script to add Teacher entity and ensure Student data is preserved.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Upgrade the database schema to include the teachers table and ensure existing data is preserved.
    '''
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )
    # Ensure existing tables for students and courses are not affected
def downgrade():
    '''
    Downgrade the database schema by dropping the association table and the teachers table.
    '''
    op.drop_table('teachers')