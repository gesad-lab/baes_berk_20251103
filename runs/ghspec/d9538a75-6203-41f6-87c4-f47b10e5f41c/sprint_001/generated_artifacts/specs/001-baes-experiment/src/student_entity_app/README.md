```plaintext
# Student Entity Application

## Description
This application provides an API for managing student records. It allows users to create new students and retrieve existing records.

## Setup Instructions
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python src/app.py
   ```

5. Initialize the database (it will initialize automatically every time the application starts).

## API Endpoints
### Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string"  // Required field
  }
  ```
- **Response**:
  - Status Code: `201 Created`
  - Body: `{"id": 1, "name": "John Doe"}` (example)

### Retrieve Students
- **Endpoint**: `GET /students`
- **Response**:
  - Status Code: `200 OK`
  - Body:
  ```json
  [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Doe"}
  ]
  ```

## Testing
To ensure at least 70% coverage of business logic, tests are implemented in the `tests/test_routes.py` file. Use the following command to run the tests:
```bash
pytest --cov=src
```

## Validation
- Ensure that you can create at least 5 students without errors.
- Assert that the API returns the correct status codes.
- Check that the responses confirm successful addition of student records in JSON format.

## Performance
- API response time should be under 200 milliseconds on average.

## Additional Information
- Documentation should include steps for any additional configurations or environments.
- Verify all functionalities manually or through Postman/curl as needed.
```