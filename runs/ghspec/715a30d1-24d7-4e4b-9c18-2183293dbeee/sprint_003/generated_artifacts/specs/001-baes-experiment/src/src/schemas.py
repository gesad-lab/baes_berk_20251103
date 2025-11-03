```python
from pydantic import BaseModel, Field, validator
from typing import Optional

class CourseCreate(BaseModel):
    name: str = Field(..., example="Mathematics 101", min_length=1, max_length=100)
    level: str = Field(..., example="Beginner", min_length=1, max_length=50)

    @validator('name')
    def validate_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Course name must not be empty.")
        return value

    @validator('level')
    def validate_level(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Course level must not be empty.")
        return value

class CourseOut(BaseModel):
    id: int
    name: str
    level: str

    class Config:
        orm_mode = True
```