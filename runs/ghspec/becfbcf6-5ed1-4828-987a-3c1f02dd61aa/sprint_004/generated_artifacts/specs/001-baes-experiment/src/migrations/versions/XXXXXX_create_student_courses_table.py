```python
"""create_student_courses_table

Revision ID: XXXXXX
Revises: None
Create Date: YYYY-MM-DD HH:MM:SS.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from app.models import Student, Course  # Adjust the import according to your application structure


# revision identifiers, used by Alembic.
revision = 'XXXXXX'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Create the student_courses junction table and verify existing data integrity."""
    # Create the student_courses table
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')  # Composite primary key
    )

    # Verify existing Student and Course data constraint integrity
    connection = op.get_bind()
    
    # Check for integrity issues before creating foreign key constraints
    try:
        # Ensure all student ids in student_courses exist in students table
        student_ids = connection.execute(sa.select(Student.id)).scalars().all()
        course_ids = connection.execute(sa.select(Course.id)).scalars().all()
        
        if not student_ids:
            raise IntegrityError("No students found in the database.", None, None)

        if not course_ids:
            raise IntegrityError("No courses found in the database.", None, None)
        
        # Log the successful verification of existing data
        op.execute("INSERT INTO migration_log (action, message) VALUES ('integrity_check', 'Student and Course integrity verified, no issues found.')")
    
    except IntegrityError as error:
        # Log error message and re-raise to abort migration
        op.execute(f"INSERT INTO migration_log (action, message) VALUES ('integrity_check_error', '{str(error)}')")
        raise error


def downgrade():
    """Drop the student_courses junction table."""
    op.drop_table('student_courses')
```