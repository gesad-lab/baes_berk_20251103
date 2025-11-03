```python
from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table, MetaData

def upgrade(migrate_engine):
    """
    Upgrade the database schema by adding the `teacher_id` foreign key column 
    to the existing `courses` table.
    
    :param migrate_engine: An instance of the SQLAlchemy Engine
    """
    meta = MetaData(bind=migrate_engine)
    courses = Table('courses', meta, autoload=True)
    
    # Adding new column `teacher_id`, referencing the `id` column in `teachers` table
    teacher_id_col = Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
    teacher_id_col.create(courses)

def downgrade(migrate_engine):
    """
    Downgrade the database schema by removing the `teacher_id` column 
    from the `courses` table.
    
    :param migrate_engine: An instance of the SQLAlchemy Engine
    """
    meta = MetaData(bind=migrate_engine)
    courses = Table('courses', meta, autoload=True)
    
    # Dropping the column if it exists
    if hasattr(courses.c, 'teacher_id'):
        courses.c.teacher_id.drop()
```