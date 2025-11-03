from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '202310xx_add_courses_table'
down_revision = None  # Update this if there is a previous migration
branch_labels = None
depends_on = None


def upgrade():
    """Create the courses table in the database schema."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),  # Name of the course, required field
        sa.Column('level', sa.String(), nullable=False)  # Level of the course, required field
    )


def downgrade():
    """Drop the courses table from the database schema."""
    op.drop_table('courses')