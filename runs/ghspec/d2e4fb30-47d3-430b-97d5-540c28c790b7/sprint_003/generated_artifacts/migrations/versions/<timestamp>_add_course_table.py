from alembic import op
import sqlalchemy as sa

# Migration script to add "Course" table
# Revision identifiers, used by Alembic.
revision = '<timestamp>_add_course_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('level', sa.String(length=255), nullable=False)
    )

def downgrade():
    # Drop the courses table
    op.drop_table('courses')