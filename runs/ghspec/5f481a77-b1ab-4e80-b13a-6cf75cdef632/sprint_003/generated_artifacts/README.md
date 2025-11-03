# File: README.md

## Project Documentation

### API Endpoints

#### Create Course

- **Endpoint**: `POST /courses`
- **Request Body**:
    ```json
    {
        "name": "Course Name",
        "level": "Beginner"
    }
    ```
- **Response**:
    - **201 Created**:
        ```json
        {
            "id": 1,
            "name": "Course Name",
            "level": "Beginner"
        }
        ```
    - **400 Bad Request**:
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Invalid input: 'name' and 'level' are required."
            }
        }
        ```

#### Retrieve Course by ID

- **Endpoint**: `GET /courses/{id}`
- **Response**:
    - **200 OK**:
        ```json
        {
            "id": 1,
            "name": "Course Name",
            "level": "Beginner"
        }
        ```
    - **404 Not Found**:
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Course not found."
            }
        }
        ```

### Database Migration Instructions

To incorporate the new `Course` entity into the existing SQLite database schema:

1. **Create Migration Script**:
   Create a new migration SQL file that includes the following SQL statement:
   ```sql
   CREATE TABLE courses (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name VARCHAR(100) NOT NULL,
       level VARCHAR(50) NOT NULL
   );
   ```
   This script creates a `Course` table with the required fields, ensuring that both `name` and `level` are not null.

2. **Run Migration**:
   Execute the migration script on your SQLite database to add the `Course` table. Ensure that this process does not interfere with any existing data in the `Student` table or other tables.

3. **Testing**:
   After running the migration, validate that the new `Course` table is correctly added. You should also run existing tests to confirm that no existing functionality is broken.

### JSON Response Format

All API responses will be in JSON format, including both success and error messages. Ensure your API handles errors gracefully, returning structured error messages that include appropriate error codes for debugging purposes.