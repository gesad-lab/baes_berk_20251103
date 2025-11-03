```python
from sqlalchemy import create_engine, Column, Integer, ForeignKey, MetaData, Table

def upgrade(migrate_engine):
    """Add teacher_id column to courses table."""
    meta = MetaData(bind=migrate_engine)
    # Autoload the existing 'courses' table
    courses = Table('courses', meta, autoload=True)
    
    # Create new column 'teacher_id' as a foreign key referencing the 'teachers' table
    if not hasattr(courses.c, 'teacher_id'):
        # Add the new column
        teacher_id_column = Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
        teacher_id_column.create(courses)

def downgrade(migrate_engine):
    """Drop teacher_id column from courses table."""
    meta = MetaData(bind=migrate_engine)
    # Autoload the existing 'courses' table
    courses = Table('courses', meta, autoload=True)
    
    # Check if the 'teacher_id' column exists before trying to drop it
    if hasattr(courses.c, 'teacher_id'):
        # Drop the column if it exists
        courses.c.teacher_id.drop()
```