'''
Create a new migration script using Alembic to add email field to students and preserve existing data.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Add email column with a default value to avoid migration issues
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, you can set a default value for existing records
    op.execute("UPDATE students SET email='default@example.com' WHERE email IS NULL")
    # Change the column to be non-nullable after setting default values
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')