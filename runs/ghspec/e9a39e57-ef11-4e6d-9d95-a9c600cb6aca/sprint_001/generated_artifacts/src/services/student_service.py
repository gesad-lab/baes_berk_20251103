```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

def validate_student_name(name: str) -> None:
    """
    Validates the student's name to ensure it is not None or empty.
    
    Parameters:
    - name (str): The name of the student to validate.
    
    Raises:
    ValueError: If the name is None or an empty string.
    """
    if name is None or name.strip() == '':
        raise ValueError("E001: Student name cannot be null or empty.")

# Example usage:
# try:
#     validate_student_name("")
# except ValueError as e:
#     print(e)  # This will print "E001: Student name cannot be null or empty."
```