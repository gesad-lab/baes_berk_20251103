```python
# migrations/001_create_student_courses_table.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table
from alembic import op
import sqlalchemy as sa

# Define a new table for the many-to-many relationship between students and courses
student_courses_table = Table(
    'student_courses',
    sa.MetaData(),
    Column('student_id', Integer, ForeignKey("students.id"), primary_key=True),
    Column('course_id', Integer, ForeignKey("courses.id"), primary_key=True)
)

def upgrade():
    # Create the student_courses table in the database
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey("students.id"), primary_key=True),
        Column('course_id', Integer, ForeignKey("courses.id"), primary_key=True)
    )

def downgrade():
    # Drop the student_courses table if we need to revert the migration
    op.drop_table('student_courses')
```