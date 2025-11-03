```python
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Ensure the new Teacher model inherits from Base
Base = declarative_base()

class Teacher(Base):
    """Represents a teacher in the database."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

class TeacherCreateRequest(BaseModel):
    """Model for creating a new teacher."""
    
    name: str = Field(..., title="Teacher Name", description="The name of the teacher.")
    email: EmailStr = Field(..., title="Email", description="The email address of the teacher.")

class TeacherResponse(BaseModel):
    """Model for returning teacher details."""
    
    id: int
    name: str
    email: str
```