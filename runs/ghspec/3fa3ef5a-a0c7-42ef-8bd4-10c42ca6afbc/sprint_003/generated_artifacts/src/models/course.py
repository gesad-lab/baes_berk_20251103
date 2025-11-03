```python
from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel, Field, ValidationError
from typing import Any

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

class CourseCreateRequest(BaseModel):
    name: str = Field(..., title="Course Name", description="The name of the course.")
    level: str = Field(..., title="Course Level", description="The level of the course.")

    # Validator to ensure that name and level are of type string
    @classmethod
    def validate(cls, value: Any):
        try:
            return cls(**value)
        except ValidationError as e:
            raise ValueError(f"Invalid course data: {e.errors()}")

# Additional methods for Course can be added below
```