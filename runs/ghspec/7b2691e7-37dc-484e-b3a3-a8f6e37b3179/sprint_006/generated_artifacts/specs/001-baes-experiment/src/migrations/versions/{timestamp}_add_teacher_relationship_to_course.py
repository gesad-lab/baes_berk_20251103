from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'timestamp'
down_revision = 'previous_revision_id'  # Replace with the actual previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Apply database schema update to add a foreign key relationship from Course to Teacher."""
    # Adding the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Creating a foreign key constraint linking the teacher_id in courses table to id in teachers table
    op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', 'teacher_id', 'id')


def downgrade():
    """Revert database schema update by removing the foreign key and column."""
    # Dropping the foreign key constraint
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')

    # Dropping the teacher_id column from the courses table
    op.drop_column('courses', 'teacher_id')