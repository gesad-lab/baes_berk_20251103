import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

def test_get_items(setup_database):
    """Test that the /items endpoint returns a list of items."""
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list), "Expected a list of items"

def test_create_item(setup_database):
    """Test that the /items endpoint can create a new item."""
    item_data = {"name": "New Item", "description": "A test item"}
    response = client.post("/items", json=item_data)
    assert response.status_code == 201
    created_item = response.json()
    assert created_item["name"] == item_data["name"]
    assert created_item["description"] == item_data["description"]

def test_get_item(setup_database):
    """Test that an item can be retrieved by ID."""
    response = client.get("/items/1")  # Assuming an item with ID 1 exists
    assert response.status_code == 200
    item = response.json()
    assert item["id"] == 1  # Adjust based on your actual setup

def test_update_item(setup_database):
    """Test that an item can be updated."""
    updated_data = {"name": "Updated Item", "description": "An updated test item"}
    response = client.put("/items/1", json=updated_data)  # Assuming an item with ID 1 exists
    assert response.status_code == 200
    updated_item = response.json()
    assert updated_item["name"] == updated_data["name"]
    assert updated_item["description"] == updated_data["description"]

def test_delete_item(setup_database):
    """Test that an item can be deleted."""
    response = client.delete("/items/1")  # Assuming an item with ID 1 exists
    assert response.status_code == 204
    # Verify that the item was deleted
    response = client.get("/items/1")
    assert response.status_code == 404  # The item should no longer exist

def test_create_item_invalid_data(setup_database):
    """Test that creating an item with invalid data returns a validation error."""
    item_data = {"name": "Invalid Item"}  # Missing required 'description'
    response = client.post("/items", json=item_data)
    assert response.status_code == 400
    assert "detail" in response.json()  # Check for validation error detail