```python
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models import Teacher

class TeacherSchema(SQLAlchemyAutoSchema):
    """Schema for the Teacher model, used for serialization and deserialization."""
    
    class Meta:
        model = Teacher
        fields = ("id", "name", "email")
```