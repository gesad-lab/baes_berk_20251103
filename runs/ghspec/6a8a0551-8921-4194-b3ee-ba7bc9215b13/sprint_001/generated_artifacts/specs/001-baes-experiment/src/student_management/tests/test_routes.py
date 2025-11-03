```python
import pytest
from marshmallow import Schema, fields, ValidationError

# Define StudentSchema using Marshmallow
class StudentSchema(Schema):
    """Schema for serializing and deserializing Student objects."""

    id = fields.Int(dump_only=True)  # auto-generated ID, read-only
    name = fields.Str(required=True, error_messages={"required": "Name is required."})

# Tests for StudentSchema
def test_valid_student_data():
    schema = StudentSchema()
    data = {'name': 'John Doe'}
    result = schema.load(data)
    assert result['name'] == 'John Doe'

def test_missing_name():
    schema = StudentSchema()
    with pytest.raises(ValidationError) as excinfo:
        schema.load({})
    assert excinfo.value.messages == {"name": ["Name is required."]}
```