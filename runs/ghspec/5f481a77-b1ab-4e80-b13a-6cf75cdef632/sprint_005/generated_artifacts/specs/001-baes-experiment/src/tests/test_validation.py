```python
import pytest
from src.schemas import TeacherSchema  # Assuming TeacherSchema exists
from marshmallow.exceptions import ValidationError

class TestTeacherValidation:
    @pytest.fixture
    def teacher_schema(self):
        """Fixture to provide a Teacher schema instance for testing."""
        return TeacherSchema()

    def test_valid_teacher_data(self, teacher_schema):
        """Test valid teacher data."""
        valid_data = {
            "name": "Jane Doe",
            "email": "jane.doe@example.com"
        }
        # Validate the input data using the schema
        result = teacher_schema.load(valid_data)
        assert result == valid_data  # Ensure the result is what we expect

    def test_invalid_teacher_data_missing_name(self, teacher_schema):
        """Test invalid teacher data with missing name."""
        invalid_data = {
            "email": "jane.doe@example.com"
        }
        with pytest.raises(ValidationError) as excinfo:
            teacher_schema.load(invalid_data)
        
        # Check for specific validation error messages
        assert "name" in excinfo.value.messages

    def test_invalid_teacher_data_invalid_email(self, teacher_schema):
        """Test invalid teacher data with improperly formatted email."""
        invalid_data = {
            "name": "Jane Doe",
            "email": "jane.doe@invalid"  # Invalid email format
        }
        with pytest.raises(ValidationError) as excinfo:
            teacher_schema.load(invalid_data)
        
        # Check for specific validation error messages
        assert "email" in excinfo.value.messages
```