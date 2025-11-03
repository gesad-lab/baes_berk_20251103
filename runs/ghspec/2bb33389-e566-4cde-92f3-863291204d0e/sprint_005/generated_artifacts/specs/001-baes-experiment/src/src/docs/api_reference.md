# src/docs/api_reference.md

## API Reference

### Teacher API

#### Create a Teacher

- **Endpoint**: `POST /teachers`
- **Description**: Create a new teacher by providing the required name and email in the request body.

##### Request Body
```json
{
  "name": "string",  // Required: The name of the teacher.
  "email": "string"  // Required: The email of the teacher, must be unique.
}
```

##### Responses
- **201 Created**: Successfully created a teacher.
  - **Response Body**:
  ```json
  {
    "id": 1,          // The unique identifier for the created teacher.
    "name": "Jane Doe", // The name of the created teacher.
    "email": "jane.doe@example.com" // The email of the created teacher.
  }
  ```

- **400 Bad Request**: Validation error due to missing or incorrect fields.
  - **Response Body**:
  ```json
  {
    "error": {
      "code": "E001", // Error code indicating a validation issue.
      "message": "Name field is required." // Descriptive message explaining the error.
    }
  }
  ```

#### Error Scenarios
1. **Create Teacher with Missing Name**: If the user attempts to create a teacher without providing a name, the system should return a 400 error code with a message indicating that the name field is required.
  
2. **Create Teacher with Missing Email**: If the user attempts to create a teacher without providing an email, the system should return a 400 error code with a message indicating that the email field is required.

3. **Create Teacher with Invalid Email Format**: If the user submits an improperly formatted email address, the system should return a 400 error code indicating that the email format is invalid.

### Database Schema Changes
- **Teacher Table**: A new `Teacher` table has been created with the following attributes:
  - `id`: integer (primary key, auto-increment)
  - `name`: string (required)
  - `email`: string (required, unique)

### Migration Verification
During application startup, the database schema is updated to include the new `Teacher` table, ensuring existing data related to Students and Courses remains intact. The system successfully applies the migration without data loss.

---

This update clarifies the new teacher API endpoint within the OpenAPI documentation, reflecting the specifications provided.