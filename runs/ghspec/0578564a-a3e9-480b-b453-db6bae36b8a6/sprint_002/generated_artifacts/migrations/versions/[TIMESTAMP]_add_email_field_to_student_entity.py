from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'TIMESTAMP'  # Replace with generated timestamp
down_revision = None  # Replace with previous revision ID, if applicable
branch_ids = None
depends_on = None

def upgrade():
    """Add email field to the Student entity."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove email field from the Student entity."""
    op.drop_column('students', 'email')