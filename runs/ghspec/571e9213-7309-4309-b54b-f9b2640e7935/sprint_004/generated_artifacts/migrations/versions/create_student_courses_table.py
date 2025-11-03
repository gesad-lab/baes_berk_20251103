import sqlalchemy as sa
from alembic import op
from sqlalchemy.schema import MetaData

# Revision identifiers, used by Alembic.
revision = 'create_student_courses_table'
down_revision = None  # Change this appropriately based on your migration history
branch_labels = None
depends_on = None

# Meta data object
metadata = MetaData()

def upgrade() -> None:
    """
    Create the student_courses intermediary table to establish a many-to-many
    relationship between students and courses.
    """
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['student_id'], ['students.id'], onupdate='CASCADE', ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['course_id'], ['courses.id'], onupdate='CASCADE', ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade() -> None:
    """
    Drop the student_courses table.
    """
    op.drop_table('student_courses')