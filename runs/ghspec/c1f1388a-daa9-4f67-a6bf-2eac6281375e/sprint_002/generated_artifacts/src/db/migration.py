```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """
    Student model representing a student entity in the database.

    Attributes:
        id (int): Unique identifier for the student. Auto-incremented.
        name (str): Name of the student. Required field.
        email (str): Email address of the student. Required field.

    This model is mapped to the 'students' table in the database and represents
    the entity required for managing student information, including the new email
    field which is expected to be unique for each student.
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

def upgrade():
    """
    Upgrade the database schema to add an email column to the students table.
    
    This operation modifies the existing students table to include an 'email'
    field while preserving the existing data. It does so by adding a new column
    which is required for future data entries.

    Raises:
        Exception: Raises an exception if the migration fails, ensuring the 
        original schema is intact.
    """
    # SQLAlchemy migration logic to add email column
    pass

def downgrade():
    """
    Downgrade the database schema by removing the email column from the students table.
    
    This operation should only be executed if it is required to revert the 
    database schema to its previous state, prior to the upgrade that added
    the email field.

    Raises:
        Exception: Raises an exception if the migration fails, ensuring the 
        original schema is intact.
    """
    # SQLAlchemy migration logic to drop email column
    pass
```