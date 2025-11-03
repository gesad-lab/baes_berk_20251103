```python
import pytest
import subprocess

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    from main import app  # Importing the FastAPI application
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_list_courses(client):
    # Step 1: Create a couple of courses
    client.post('/courses', json={"name": "Physics 101", "level": "Intermediate"})
    client.post('/courses', json={"name": "Chemistry 101", "level": "Beginner"})
    
    # Step 2: Retrieve the courses
    response = client.get('/courses')
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_generate_migration_script():
    """
    Test to generate Alembic migration script for the Course table.
    This function runs the Alembic command to create a new migration script.
    """
    try:
        # Run the Alembic revision command to generate migration for Course table
        result = subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", "Create Course table"],
            check=True,
            capture_output=True,
            text=True
        )
        # Check that the command executed successfully and output the stdout
        print("Migration script generated successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Failed to generate migration script: {e.stderr}")
```