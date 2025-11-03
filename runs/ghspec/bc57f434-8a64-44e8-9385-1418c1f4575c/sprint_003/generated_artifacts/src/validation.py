```python
from pydantic import BaseModel, Field, constr

class Course(BaseModel):
    name: constr(strict=True, min_length=1) = Field(..., description="The name of the course, which must be a non-empty string.")
    level: constr(strict=True, min_length=1) = Field(..., description="The level of the course, which must be a non-empty string.")
```