from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '002_add_email_to_student'
down_revision = '001_previous_revision'  # Update with the actual previous revision ID
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Add the new 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(length=255), nullable=False))

def downgrade() -> None:
    # Remove the 'email' column in case of rollback
    op.drop_column('students', 'email')