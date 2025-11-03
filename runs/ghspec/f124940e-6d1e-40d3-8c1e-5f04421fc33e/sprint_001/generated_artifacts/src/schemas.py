```python
from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    id: int
    name: str

class StudentCreate(BaseModel):
    name: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None

class StudentListResponse(BaseModel):
    students: List[Student]

class NoContentResponse(BaseModel):
    """
    Response model to be returned for 204 No Content status.
    This does not include any data as the response indicates
    a successful operation with no additional content.
    """
    pass
```