```python
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    """Represents a Teacher entity in the database."""
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Teacher's name, required field
    email = Column(String, nullable=False)  # Teacher's email, required field

    __table_args__ = (
        UniqueConstraint('email', name='uq_teacher_email'),  # Ensure email uniqueness
    )

    def __repr__(self):
        """Return a string representation of the Teacher instance."""
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```