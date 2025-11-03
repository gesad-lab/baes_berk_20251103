from alembic import op
import sqlalchemy as sa

# Migration script to add email field to the students table
def upgrade():
    """Add email column to the students table."""
    # Adding the new email column to the existing students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove email column from the students table."""
    # Dropping the email column in case of a downgrade
    op.drop_column('students', 'email')