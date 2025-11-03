from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_create_courses_table'
down_revision = None  # Use the appropriate previous migration revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Create the courses table in the database."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    """Drop the courses table from the database."""
    op.drop_table('courses')