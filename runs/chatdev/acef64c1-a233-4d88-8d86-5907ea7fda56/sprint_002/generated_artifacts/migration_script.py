'''
Database migration script to add email column to the Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_email_to_student'
down_revision = None  # or the previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column to the students table with a default value
    op.add_column('students', sa.Column('email', sa.String(), nullable=False, server_default=''))
def downgrade():
    # Remove the email column from the students table
    op.drop_column('students', 'email')