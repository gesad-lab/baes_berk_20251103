'''
Database migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_email_to_student'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Update existing records to have a default value
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 3: Alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')