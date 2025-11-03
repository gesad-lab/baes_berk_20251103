from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, String, Column

# revision identifiers, used by Alembic.
revision = 'initial_create_courses_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    """Create the courses table."""
    op.create_table(
        'courses',
        sa.Column('id', Integer, primary_key=True, autoincrement=True),
        sa.Column('name', String, nullable=False),
        sa.Column('level', String, nullable=False)
    )

def downgrade():
    """Drop the courses table."""
    op.drop_table('courses')