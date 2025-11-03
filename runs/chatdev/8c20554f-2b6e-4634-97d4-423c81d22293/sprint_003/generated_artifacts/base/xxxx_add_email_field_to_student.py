'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    '''
    Add email column to the students table.
    '''
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    '''
    Remove email column from the students table.
    '''
    op.drop_column('students', 'email')