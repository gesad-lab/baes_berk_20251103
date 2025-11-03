# README.md

# Student Management API

This project provides a simple API for managing student records. It allows users to create, retrieve, update, and delete student information.

## Setup

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-management.git
   cd student-management
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry init
   poetry add fastapi[all] sqlalchemy pytest
   ```

3. Create a `.env` file based on the `.env.example` for any necessary configuration.

4. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

## API Endpoints

### Create Student
- **POST** `/students`
- Request Body: `{ "name": "string" }`
- Response: JSON representation of the created student with unique ID.

### Retrieve Student
- **GET** `/students/{id}`
- Response: JSON representation of the student if found, or an error message if not found.

### Update Student
- **PUT** `/students/{id}`
- Request Body: `{ "name": "string" }`
- Response: JSON representation of the updated student or an error message.

### Delete Student
- **DELETE** `/students/{id}`
- Response: Confirmation message or an error message if student is not found.

## Error Handling

The application handles invalid requests with meaningful error messages for invalid inputs, such as:
- Empty `name` when creating or updating a student.
- Non-existent student ID when retrieving or deleting a student.

## Testing Error Handling

### Test Cases for Error Handling

Here are the test cases for validating error handling in the API:

1. **Create Student with Empty Name**
   - Request: `POST /students` with body `{ "name": "" }`
   - Expected Response: `400 Bad Request` with error message `"E001: Name cannot be empty"`

2. **Retrieve Non-Existent Student**
   - Request: `GET /students/999` (Assuming no student with ID 999 exists)
   - Expected Response: `404 Not Found` with error message `"E002: Student not found"`

3. **Update Non-Existent Student**
   - Request: `PUT /students/999` with body `{ "name": "New Name" }`
   - Expected Response: `404 Not Found` with error message `"E002: Student not found"`

4. **Update Student with Empty Name**
   - First, create a student to get a valid ID, then request: `PUT /students/{id}` with body `{ "name": "" }`
   - Expected Response: `400 Bad Request` with error message `"E001: Name cannot be empty"`

5. **Delete Non-Existent Student**
   - Request: `DELETE /students/999`
   - Expected Response: `404 Not Found` with error message `"E002: Student not found"`

## Conclusion

This API project allows you to easily manage student records. Follow the error handling test cases to ensure the application returns the correct responses for various error situations.