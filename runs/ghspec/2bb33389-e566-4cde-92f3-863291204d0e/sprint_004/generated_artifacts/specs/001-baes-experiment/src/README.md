# Updated README.md

# Project Title

## Description

This project is a FastAPI application that allows for student-course enrollment management. Users can create, read, update, and delete courses and enroll students in these courses through a set of defined endpoints.

## Endpoints

### Student-Course Enrollment Endpoints

#### Enroll a Student in a Course

- **Endpoint**: `/enrolments`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "student_id": "string",  // ID of the student
    "course_id": "string"    // ID of the course
  }
  ```
- **Responses**:
  - **201 Created**: Student successfully enrolled.
  - **400 Bad Request**: Invalid input.
  - **404 Not Found**: Student or course ID does not exist.

#### Get All Enrollments

- **Endpoint**: `/enrolments`
- **Method**: `GET`
- **Responses**:
  - **200 OK**: Returns a list of enrollments.
  - **500 Internal Server Error**: Some error occurred on the server.

#### Get Enrollment by ID

- **Endpoint**: `/enrolments/{enrollment_id}`
- **Method**: `GET`
- **Responses**:
  - **200 OK**: Returns the enrollment details.
  - **404 Not Found**: Enrollment ID not found.

#### Delete an Enrollment

- **Endpoint**: `/enrolments/{enrollment_id}`
- **Method**: `DELETE`
- **Responses**:
  - **204 No Content**: Enrollment successfully deleted.
  - **404 Not Found**: Enrollment ID not found.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, use the following command:

```bash
uvicorn src.api:app --reload
```

Visit `http://127.0.0.1:8000`, where the API documentation is available at `http://127.0.0.1:8000/docs`.

## Testing

To run the tests, ensure you have installed the testing dependencies and then run:

```bash
pytest
```

## Contributing

We welcome contributions! Please submit a pull request for any enhancements or fixes you suggest.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.