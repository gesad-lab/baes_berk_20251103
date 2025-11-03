```python
import logging

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", "context": "%(name)s"}'
)
logger = logging.getLogger(__name__)

class Student:
    """Student entity with ORM functionality."""
    
    def __init__(self, name: str):
        if not name:
            logger.error('Failed to create student: name is required', extra={'context': 'Student'})
            raise ValueError('Name is required')
        self.name = name
        logger.info('Student created successfully', extra={'context': 'Student', 'name': self.name})

    def __repr__(self):
        return f"Student(name={self.name})"
```