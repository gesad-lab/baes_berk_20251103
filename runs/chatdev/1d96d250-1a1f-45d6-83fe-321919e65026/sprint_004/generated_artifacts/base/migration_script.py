'''
Database migration script to add courses table.
'''
from sqlalchemy import Column, String
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_courses_table'
down_revision = 'add_email_column'
branch_labels = None
depends_on = None
def upgrade():
    '''
    Upgrade the database schema to add the courses table.
    '''
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
def downgrade():
    '''
    Downgrade the database schema by removing the courses table.
    '''
    op.drop_table('courses')