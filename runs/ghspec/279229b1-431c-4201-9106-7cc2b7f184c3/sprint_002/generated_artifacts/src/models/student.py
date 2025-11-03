```python
from sqlalchemy import Column, Integer, String
from your_app_name import Base  # Adjust according to your application structure

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field added

    def __init__(self, name: str, email: str):
        """
        Initializes a new Student instance.

        :param name: The name of the student.
        :param email: The email of the student.
        """
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

    # Other methods...
```