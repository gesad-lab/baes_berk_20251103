from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_relationship_to_course'
down_revision = None  # Use the appropriate previous migration revision number
branch_labels = None
depends_on = None


def upgrade():
    """Add teacher_id column to courses table."""
    # Adding the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Creating a foreign key constraint linking teacher_id to teachers table
    op.create_foreign_key(
        'fk_course_teacher',  # Name of the foreign key
        'courses',            # Source table
        'teachers',           # Referenced table
        ['teacher_id'],       # Source column
        ['id'],               # Referenced column
        ondelete='SET NULL'   # When a teacher is deleted, set this column to NULL
    )


def downgrade():
    """Remove teacher_id column from courses table."""
    # Dropping the foreign key constraint
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')

    # Dropping the teacher_id column
    op.drop_column('courses', 'teacher_id')