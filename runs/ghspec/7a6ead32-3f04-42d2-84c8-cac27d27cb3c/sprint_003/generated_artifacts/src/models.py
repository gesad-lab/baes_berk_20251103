```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    """Model representing a Course entity."""
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    @classmethod
    def validate_name_and_level(cls, name: str, level: str) -> bool:
        """Validates that name and level are provided.
        
        Args:
            name (str): The name of the course.
            level (str): The level of the course.

        Returns:
            bool: True if both name and level are non-empty, otherwise False.
        """
        return bool(name and level)
```