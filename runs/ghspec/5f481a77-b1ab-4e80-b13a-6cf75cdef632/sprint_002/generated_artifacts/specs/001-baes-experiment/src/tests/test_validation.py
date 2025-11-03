import pytest
from src.schemas import StudentSchema
from marshmallow.exceptions import ValidationError

class TestValidation:
    @pytest.fixture
    def student_schema(self):
        """Fixture to provide a Student schema instance for testing."""
        return StudentSchema()

    def test_valid_student_data(self, student_schema):
        """Test valid student data"""
        valid_data = {
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
        # Validate should pass with valid data
        result = student_schema.load(valid_data)
        assert result['name'] == valid_data['name']
        assert result['email'] == valid_data['email']

    def test_missing_name(self, student_schema):
        """Test missing name raises ValidationError"""
        invalid_data = {
            "email": "jane.doe@example.com"
        }
        with pytest.raises(ValidationError) as exc_info:
            student_schema.load(invalid_data)
        assert "missing" in str(exc_info.value)

    def test_missing_email(self, student_schema):
        """Test missing email raises ValidationError"""
        invalid_data = {
            "name": "Jane Doe"
        }
        with pytest.raises(ValidationError) as exc_info:
            student_schema.load(invalid_data)
        assert "missing" in str(exc_info.value)

    def test_invalid_email_format(self, student_schema):
        """Test invalid email format raises ValidationError"""
        invalid_data = {
            "name": "John Doe",
            "email": "invalid-email"
        }
        with pytest.raises(ValidationError) as exc_info:
            student_schema.load(invalid_data)
        assert "not a valid email address" in str(exc_info.value)

    def test_empty_email(self, student_schema):
        """Test empty email raises ValidationError"""
        invalid_data = {
            "name": "John Doe",
            "email": ""
        }
        with pytest.raises(ValidationError) as exc_info:
            student_schema.load(invalid_data)
        assert "Field may not be blank." in str(exc_info.value)