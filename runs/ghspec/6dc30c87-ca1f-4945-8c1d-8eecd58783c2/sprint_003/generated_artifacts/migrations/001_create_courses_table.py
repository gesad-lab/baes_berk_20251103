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

    @validates('name', 'level')
    def validate_fields(self, key, value):
        """Validate that name and level fields are not empty."""
        if not value:
            raise ValueError(f"{key} field cannot be empty.")
        return value

# Note: The rest of the necessary setup for migration should be handled separately
```