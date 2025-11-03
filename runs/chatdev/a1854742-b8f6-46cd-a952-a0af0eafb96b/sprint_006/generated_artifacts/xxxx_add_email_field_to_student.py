'''
Migration script to add email field to Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxx_add_email_field_to_student'
down_revision = None
def upgrade():
    # Add email column to the students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
def downgrade():
    # Remove email column from the students table
    op.drop_column('students', 'email')