```python
# File: migrations/versions/xxxxxx_add_teacher_id_to_courses.py

from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

# Upgrade to add teacher_id column to courses table
def upgrade():
    # Create 'teacher_id' column in 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    # Create foreign key constraint linking 'teacher_id' to 'teachers' table
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

# Downgrade to remove teacher_id column from courses table
def downgrade():
    # Drop the foreign key constraint
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    # Drop the 'teacher_id' column
    op.drop_column('courses', 'teacher_id')

def remove_teacher_from_course(course_id: int):
    """
    Remove the association of a teacher from a specific course.

    Parameters:
    - course_id (int): The ID of the course from which to remove the teacher.

    Raises:
    - HTTPException: If course does not exist or an error occurs during the operation.
    """
    # Import Session and Course from your models
    from src.model import Session, Course
    from fastapi import HTTPException

    session = Session()
    try:
        # Fetch the course by ID
        course = session.query(Course).filter(Course.id == course_id).one_or_none()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")

        # Dissociate the teacher by setting teacher_id to None
        course.teacher_id = None
        session.commit()

    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Error removing teacher: {str(e)}")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        session.close()
```