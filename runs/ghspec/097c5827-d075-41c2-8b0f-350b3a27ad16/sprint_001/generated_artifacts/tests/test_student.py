```python
import pytest
from flask import json
from src.app import app
from src.models import Student

@pytest.fixture
def client():
    """Create a test client for the application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_student_without_name(client):
    """Test case for attempting to create a Student without a name."""
    
    # Attempt to create a student without a name
    response = client.post('/students', data=json.dumps({'name': ''}), content_type='application/json')
    
    # Assert a 400 Bad Request response
    assert response.status_code == 400
    
    # Check the error response structure
    response_data = json.loads(response.data)
    assert 'error' in response_data
    assert response_data['error']['code'] == 'E001'  # Example error code for missing name
    assert response_data['error']['message'] == 'Name field is required.'
```
