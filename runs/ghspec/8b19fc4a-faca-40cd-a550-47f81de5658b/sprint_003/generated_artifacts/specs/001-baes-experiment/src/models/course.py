```python
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Course(Base):
    """Course model to store course information."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    @validates('name', 'level')
    def validate_not_empty(self, key, value):
        """Validate that name and level fields are not empty."""
        if not value:
            raise ValueError(f"{key} must not be empty.")
        return value

    def to_dict(self):
        """Convert Course instance to dictionary representation."""
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level
        }
```