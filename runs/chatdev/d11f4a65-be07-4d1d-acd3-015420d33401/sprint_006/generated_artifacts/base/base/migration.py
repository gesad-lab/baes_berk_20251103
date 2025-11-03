'''
Migration script to add email column to the students table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with your revision ID
down_revision = None  # Replace with your down revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Add email column to the students table as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
def downgrade():
    # Remove email column from the students table
    op.drop_column('students', 'email')