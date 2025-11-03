'''
Database migration script to add teachers table.
'''
from sqlalchemy import Column, String, Integer
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teachers_table'
down_revision = 'add_courses_table_and_association'
branch_labels = None
depends_on = None
def upgrade():
    '''
    Upgrade the database schema to add the teachers table.
    '''
    # Check if the teachers table already exists
    if not op.get_bind().has_table('teachers'):
        op.create_table(
            'teachers',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False),
            sa.PrimaryKeyConstraint('id')
        )
def downgrade():
    '''
    Downgrade the database schema by removing the teachers table.
    '''
    op.drop_table('teachers')