# README.md

# Project Title

## Description
This project is designed to manage student-course relationships through a FastAPI application. It allows users to create courses, enroll students, and manage the course roster effectively.

## Deployment Considerations
- The application will run locally using Uvicorn as the ASGI server. You can start the server using the following command:
  ```bash
  uvicorn main:app --reload
  ```

## Features
### Student-Course Relationship Functionality

#### Endpoints
1. **Create Course**
   - **Endpoint**: `/courses/create`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "name": "Course Name",
       "description": "Course Description",
       "credit_hours": 3
     }
     ```
   - **Response**:
     - **201 Created**: Returns the created course object.
     - **400 Bad Request**: If required fields are missing or invalid.

2. **Enroll Student in Course**
   - **Endpoint**: `/courses/enroll`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "student_id": 1,
       "course_id": 1
     }
     ```
   - **Response**:
     - **200 OK**: Returns enrollment details.
     - **404 Not Found**: If the student or course does not exist.
     - **400 Bad Request**: If the request format is incorrect.

3. **Get Course Roster**
   - **Endpoint**: `/courses/roster/{course_id}`
   - **Method**: `GET`
   - **Response**:
     - **200 OK**: Returns a list of enrolled students in the course.
     - **404 Not Found**: If the course does not exist.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   (Include specific instructions if required)

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Testing
To run the tests for the student-course functionality, execute:
```bash
pytest tests/
```

## Contributing
We welcome contributions! Please create a pull request with a clear description of your changes and why they are needed.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.