```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    VALID_LEVELS = {"Beginner", "Intermediate", "Advanced"}

    @validates('name')
    def validate_name(self, key, value):
        """Validate that name is a non-empty string."""
        if not value or not isinstance(value, str):
            raise ValueError("Name is required and must be a string.")
        return value

    @validates('level')
    def validate_level(self, key, value):
        """Validate that level is one of the valid options."""
        if value not in self.VALID_LEVELS:
            raise ValueError(f"Level must be one of {', '.join(self.VALID_LEVELS)}.")
        return value
```