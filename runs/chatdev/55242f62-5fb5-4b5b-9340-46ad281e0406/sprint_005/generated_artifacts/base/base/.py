'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None  # Replace with the previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))  # Add email column
def downgrade():
    op.drop_column('students', 'email')  # Remove email column if needed