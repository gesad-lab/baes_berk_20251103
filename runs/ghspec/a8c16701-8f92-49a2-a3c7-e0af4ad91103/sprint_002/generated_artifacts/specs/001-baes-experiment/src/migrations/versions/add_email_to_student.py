from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'add_email_to_student'
down_revision = None  # Change this to the last migration's revision identifier if applicable
branch_labels = None
depends_on = None


def upgrade():
    """Add the email column to the students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Remove the email column from the students table."""
    op.drop_column('students', 'email')