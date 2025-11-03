'''
Migration script to add Course entity and ensure Student data is preserved.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Upgrade the database schema to include the courses table.
    '''
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    '''
    Downgrade the database schema by dropping the courses table.
    '''
    op.drop_table('courses')