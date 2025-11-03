from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr, validator

Base = declarative_base()

class Teacher(Base):
    """Model representing a Teacher entity."""
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)


class TeacherCreateRequest(BaseModel):
    """Pydantic model for creating a new Teacher."""
    name: str
    email: EmailStr

    @validator('name')
    def check_name(cls, v):
        """Validate that the name field is not empty."""
        if not v:
            raise ValueError('Name field is required.')
        return v