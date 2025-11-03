from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'create_courses_table'
down_revision = None  # Change this if there's a previous revision
branch_labels = None
depends_on = None


def upgrade():
    """Create the courses table in the database."""
    op.create_table(
        'courses',  # Name of the table
        sa.Column('id', sa.Integer, primary_key=True),  # Primary key
        sa.Column('name', sa.String, nullable=False),  # Course name, required
        sa.Column('level', sa.String, nullable=False)  # Course level, required
    )


def downgrade():
    """Drop the courses table from the database."""
    op.drop_table('courses')  # Dropping the courses table during downgrade