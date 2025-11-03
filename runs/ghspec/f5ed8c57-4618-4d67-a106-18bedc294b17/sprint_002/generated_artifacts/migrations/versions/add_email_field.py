from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20230101010101'  # Replace with the appropriate revision ID
down_revision = '20221231121212'  # Replace with the previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Add email field to the students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    # Optionally, if needed, add a unique constraint to ensure email uniqueness
    op.create_unique_constraint('uq_students_email', 'students', ['email'])


def downgrade():
    """Remove email field from the students table."""
    op.drop_column('students', 'email')