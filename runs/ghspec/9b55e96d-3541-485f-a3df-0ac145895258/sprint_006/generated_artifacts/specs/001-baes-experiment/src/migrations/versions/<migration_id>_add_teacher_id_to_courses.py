from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '<migration_id>'  # Use a unique identifier for the migration
down_revision = None  # Set to the previous migration ID if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to courses table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

def downgrade():
    """Remove teacher_id column from courses table."""
    op.drop_column('courses', 'teacher_id')