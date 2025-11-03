from alembic import op
import sqlalchemy as sa


def upgrade():
    """Add email field to the students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    """Remove email field from the students table."""
    op.drop_column('students', 'email')