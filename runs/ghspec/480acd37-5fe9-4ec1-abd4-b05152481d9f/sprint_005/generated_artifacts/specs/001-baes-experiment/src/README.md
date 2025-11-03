# Updated README.md

# Teacher Management App

This application provides an API for managing teachers and students. It allows for the creation and retrieval of teacher entities while maintaining strict validation rules.

## API Endpoints

### Teacher Endpoints

#### POST /teachers
Create a new teacher in the system.

- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```

- **Response**:
  - **201 Created**: Returns the created teacher object.
  
```json
{
  "id": 1,
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

- **Error Responses**:
  - **400 Bad Request**: If name or email is missing.
  - **409 Conflict**: If the email already exists.

#### GET /teachers
Retrieve all registered teachers.

- **Response**:
  - **200 OK**: Returns an array of teacher objects.

```json
[
  {
    "id": 1,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  },
  {
    "id": 2,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
]
```

## Usage Examples

### Creating a Teacher
To create a new teacher, send a `POST` request to the `/teachers` endpoint with the required JSON body:

```bash
curl -X POST http://localhost:8000/teachers \
-H "Content-Type: application/json" \
-d '{"name": "Jane Smith", "email": "jane.smith@example.com"}'
```

### Retrieving Teachers
To retrieve all teachers, send a `GET` request to the `/teachers` endpoint:

```bash
curl http://localhost:8000/teachers
```

## Running the Application

1. Ensure that you have the required dependencies installed. Check `requirements.txt` for a list of packages needed.
2. Run the application:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

3. Access the API via `http://localhost:8000`.

## Database Migrations

The application requires a database migration to create a new `teachers` table. This migration can be run using Alembic, ensuring it does not affect existing tables (like students and courses).

## Conclusion

This README provides essential information regarding the new teacher management feature, API endpoints, usage examples, and setup instructions. Ensure to follow the instructions adequately to access the updated features of the application.