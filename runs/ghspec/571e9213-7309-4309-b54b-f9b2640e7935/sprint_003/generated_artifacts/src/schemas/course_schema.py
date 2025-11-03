```python
from pydantic import BaseModel, Field, constr
from typing import Optional

class CourseSchema(BaseModel):
    id: Optional[int]  # Optional for request, required in response
    name: constr(min_length=1)  # Required field with a minimum length of 1
    level: constr(min_length=1)  # Required field with a minimum length of 1

    class Config:
        orm_mode = True
```