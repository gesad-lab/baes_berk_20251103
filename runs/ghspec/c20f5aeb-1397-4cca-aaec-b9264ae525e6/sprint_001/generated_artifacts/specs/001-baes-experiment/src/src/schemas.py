```python
from pydantic import BaseModel, validator, ValidationError

class StudentBase(BaseModel):
    name: str

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or not v.strip():  # Check for non-empty and non-whitespace string
            raise ValueError('Name must not be empty')
        return v

# Other schemas or models can be defined below
```