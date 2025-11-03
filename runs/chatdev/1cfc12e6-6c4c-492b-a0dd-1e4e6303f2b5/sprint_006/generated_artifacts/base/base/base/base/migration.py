'''
Database migration script to add email field to the Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Add email column to students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    # Remove email column from students table
    op.drop_column('students', 'email')