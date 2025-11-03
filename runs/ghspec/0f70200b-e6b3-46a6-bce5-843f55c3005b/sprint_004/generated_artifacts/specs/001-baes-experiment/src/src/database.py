```python
# src/database.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from alembic import op
import sqlalchemy as sa

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    # Other fields remain unchanged...

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    # Other fields remain unchanged...

# Many-to-many relationship between students and courses
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

def init_db():
    """Initialize the database and run migrations."""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    # Running migrations
    alembic_cfg = Config("alembic.ini")
    with engine.begin() as connection:
        command.upgrade(alembic_cfg, 'head')  # Ensure migrations are applied

def downgrade():
    """Remove the student_courses table during downgrade."""
    with op.batch_alter_table('student_courses') as batch_op:
        # Drop constraint before removing the table
        batch_op.drop_constraint('student_courses_student_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('student_courses_course_id_fkey', type_='foreignkey')
    op.drop_table('student_courses')  # Safely drop the table
```