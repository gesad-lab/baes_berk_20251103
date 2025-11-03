'''
Database migration script to add email column to the students table.
'''
from sqlalchemy import Column, String
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_email_column'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    '''
    Upgrade the database schema to add the email column.
    '''
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    '''
    Downgrade the database schema by removing the email column.
    '''
    op.drop_column('students', 'email')