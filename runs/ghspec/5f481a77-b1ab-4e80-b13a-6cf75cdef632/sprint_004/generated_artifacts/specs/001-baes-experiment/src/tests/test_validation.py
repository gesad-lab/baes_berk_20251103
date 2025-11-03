```python
import pytest
from src.schemas import CourseSchema  # Assuming CourseSchema exists
from marshmallow.exceptions import ValidationError

class TestCourseValidation:
    @pytest.fixture
    def course_schema(self):
        """Fixture to provide a Course schema instance for testing."""
        return CourseSchema()

    def test_valid_course_data(self, course_schema):
        """Test valid course data."""
        valid_data = {
            "name": "Introduction to Programming",
            "level": "Beginner"
        }
        # Validate the course data using the schema
        assert course_schema.load(valid_data) == valid_data

    def test_invalid_course_data_missing_name(self, course_schema):
        """Test invalid course data when the name is missing."""
        invalid_data = {
            "level": "Beginner"
        }
        with pytest.raises(ValidationError) as excinfo:
            course_schema.load(invalid_data)
        assert "name" in excinfo.value.messages  # Check for validation error on 'name'

    def test_invalid_course_data_empty_name(self, course_schema):
        """Test invalid course data when the name is empty."""
        invalid_data = {
            "name": "",
            "level": "Beginner"
        }
        with pytest.raises(ValidationError) as excinfo:
            course_schema.load(invalid_data)
        assert "name" in excinfo.value.messages  # Check for validation error on 'name'

    def test_invalid_course_data_invalid_level(self, course_schema):
        """Test invalid course data when level is not allowed."""
        invalid_data = {
            "name": "Advanced Mathematics",
            "level": "Expert"  # Assuming 'Beginner' and 'Intermediate' are valid levels
        }
        with pytest.raises(ValidationError) as excinfo:
            course_schema.load(invalid_data)
        assert "level" in excinfo.value.messages  # Check for validation error on 'level'
```