```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key

    # Establishing relationship with Teacher model
    teacher = relationship('Teacher', back_populates='courses')  # Set up relationship

    def __init__(self, name, teacher_id=None):
        self.name = name
        self.teacher_id = teacher_id
```

```python
from sqlalchemy import MigrationContext, Table, MetaData, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateTable, DropTable, AlterTable
from sqlalchemy.engine import Engine

Base = declarative_base()

def upgrade(engine: Engine):
    # Add teacher_id column to courses table
    with engine.connect() as connection:
        connection.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id)')

def downgrade(engine: Engine):
    # Drop the teacher_id column from courses table (if necessary)
    with engine.connect() as connection:
        connection.execute('ALTER TABLE courses DROP COLUMN teacher_id')
```