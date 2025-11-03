```python
from sqlalchemy import Column, Integer, String
from src.database.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

    def __repr__(self):
        return f"<Student name={self.name} email={self.email}>"
```