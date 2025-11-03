# Student Management Application

This README provides setup instructions, API usage examples, and testing instructions for the Student Management Web Application.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [repository-url]
   cd student_management_app
   ```

2. **Install dependencies:**
   Ensure you have Python 3.8+ installed, then set up a virtual environment and install dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Environment Configuration:**
   Create a `.env` file in the root directory and add necessary configuration settings. (Refer to `.env.example` for required keys).

## API Usage Examples

### Create a Student

- **Endpoint**: `/students` (POST)
- **Request Body**:
    ```json
    {
        "name": "John Doe"
    }
    ```
- **Response**:
    - **Status Code**: 201 (Created)
    - **Response Body**:
    ```json
    {
        "id": 1,
        "name": "John Doe"
    }
    ```

### Get All Students

- **Endpoint**: `/students` (GET)
- **Response**:
    - **Status Code**: 200 (OK)
    - **Response Body**:
    ```json
    [
        {
            "id": 1,
            "name": "John Doe"
        }
    ]
    ```

## Testing Instructions

To run tests for the application, use the following command:

```bash
pytest
```

Make sure that your database is initialized correctly, as tests may require a fresh state.

### Endpoint Tests

We have implemented tests for the API endpoints, including:

- `GET /students` to retrieve student data.
- `POST /students` to create new student records.

These tests can be found in `tests/test_api.py`.

## Database Schema

The application will automatically create the SQLite database schema on startup, including a `students` table with `id` and `name` fields. Ensure your database file path is correctly set in your configuration. 

### Troubleshooting

- If you encounter any issues, check the logs for detailed error messages.
- Ensure your SQLite database file is writable and correctly configured in the environment settings.

For further questions, refer to the documentation or raise an issue in the repository.