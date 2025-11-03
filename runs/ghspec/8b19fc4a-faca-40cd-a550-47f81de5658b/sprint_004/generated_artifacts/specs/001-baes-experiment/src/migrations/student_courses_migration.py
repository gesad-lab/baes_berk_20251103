```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def upgrade():
    """Create the join table for students and courses."""
    meta = MetaData(bind=engine)

    student_courses = Table(
        'student_courses',
        meta,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )

    # Create the table if it doesn't exist
    meta.create_all(engine, checkfirst=True)

def downgrade():
    """Drop the join table if it exists."""
    meta = MetaData(bind=engine)
    student_courses = Table('student_courses', meta, autoload_with=engine)
    
    # Only drop the table if it exists
    if student_courses.exists():
        student_courses.drop(engine)
```