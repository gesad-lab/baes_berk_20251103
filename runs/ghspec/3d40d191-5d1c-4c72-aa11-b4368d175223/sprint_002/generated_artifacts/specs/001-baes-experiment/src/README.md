# Updated README.md

# Project README

## Overview

This project is a FastAPI application that allows users to manage students. Users can create students, retrieve a list of students, and manage their details.

## API Endpoints

### Create Student

- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
      "name": "string",
      "email": "string"
  }
  ```
- **Response**: 
   - Status: 201 Created
   - Body: 
   ```json
   {
       "id": "int",
       "name": "string",
       "email": "string"
   }
   ```
- **Description**: This endpoint creates a new student with a name and email. Both fields are required.

### Retrieve Students

- **Endpoint**: `GET /students`
- **Response**: 
   - Status: 200 OK
   - Body: 
   ```json
   [
       {
           "id": "int",
           "name": "string",
           "email": "string"
       }
   ]
   ```
- **Description**: This endpoint retrieves a list of all students, including their names and emails.

## Error Handling

- **Missing Email**: If the `POST /students` request is made without an "email" field, the response will return:
   - Status: 400 Bad Request
   - Body: 
   ```json
   {
       "detail": "Email field is required."
   }
   ```
- **Other validations**: Similar validations should be implemented for other fields as needed.

## Local Development

To run this application locally, ensure you have Python 3.7+ installed along with the required dependencies.

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn src.api:app --reload
   ```

## Testing

To run tests, use the pytest framework. Make sure the test database is set up properly.

Run the following command to execute the tests:

```bash
pytest tests/
```

### Example Tests

Here are some example tests that have been implemented for the API:

```python
def test_create_student_with_email(client):
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "john@example.com"

def test_create_student_without_email(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email field is required."
```

## Database Configuration

The application uses SQLite as the database. Ensure that the schema is up-to-date with the required fields for the Student entity, including the newly added email field. Use migrations to apply any changes to the database schema.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.