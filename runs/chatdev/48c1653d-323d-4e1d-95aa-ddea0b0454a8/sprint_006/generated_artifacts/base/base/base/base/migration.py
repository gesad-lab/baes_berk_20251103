'''
Migration script to add email field to Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_email_to_student'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Add email column to the students table as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Populate existing records with a default email value
    connection = op.get_bind()
    connection.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    # Remove email column from the students table
    op.drop_column('students', 'email')