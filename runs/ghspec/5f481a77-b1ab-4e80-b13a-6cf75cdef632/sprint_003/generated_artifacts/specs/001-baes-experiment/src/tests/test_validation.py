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
        """Test valid course data"""
        valid_data = {
            "name": "Introduction to Programming",
            "level": "Beginner"
        }
        # Validate the data and assert no exceptions are raised
        course_schema.load(valid_data)

    def test_missing_name(self, course_schema):
        """Test that missing course name raises a validation error"""
        invalid_data = {
            "level": "Beginner"
        }
        with pytest.raises(ValidationError) as excinfo:
            course_schema.load(invalid_data)
        
        assert "name" in excinfo.value.messages

    def test_missing_level(self, course_schema):
        """Test that missing course level raises a validation error"""
        invalid_data = {
            "name": "Introduction to Programming"
        }
        with pytest.raises(ValidationError) as excinfo:
            course_schema.load(invalid_data)

        assert "level" in excinfo.value.messages

    def test_empty_name(self, course_schema):
        """Test that an empty course name raises a validation error"""
        invalid_data = {
            "name": "",
            "level": "Beginner"
        }
        with pytest.raises(ValidationError) as excinfo:
            course_schema.load(invalid_data)

        assert "name" in excinfo.value.messages

    def test_empty_level(self, course_schema):
        """Test that an empty course level raises a validation error"""
        invalid_data = {
            "name": "Introduction to Programming",
            "level": ""
        }
        with pytest.raises(ValidationError) as excinfo:
            course_schema.load(invalid_data)

        assert "level" in excinfo.value.messages
```