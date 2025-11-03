```python
"""
student.py - Model for the Student entity.

This module defines the Student class representing a student entity.
It includes validation for the name field.
"""

class Student:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Name is required.")
        self.name = name
    
    def to_dict(self):
        """Convert the Student instance to a dictionary."""
        return {"name": self.name}
```