# README.md

# Course Management API

This documentation provides an overview of the Course Management API, which allows users to create, retrieve, update, and validate course records. The API performs essential operations ensuring that courses are managed effectively.

## User Scenarios & Testing

1. **Create a Course Record**: A user can submit a request to create a new course record by providing a name and level. The system should respond with the created course data, including an ID.
   - **Endpoint**: `POST /courses`
   - **Request Body**:
     ```json
     {
       "name": "Course Name",
       "level": "Beginner"
     }
     ```
   - **Response**:
     - Status Code: `201 Created`
     - Body:
     ```json
     {
       "id": "123",
       "name": "Course Name",
       "level": "Beginner"
     }
     ```
   - **Test**: Ensure that submitting a valid course name and level creates a new course entry with both details included.

2. **Retrieve All Course Records**: A user can request a list of all course records, which should now include the name and level of each course.
   - **Endpoint**: `GET /courses`
   - **Response**:
     - Status Code: `200 OK`
     - Body:
     ```json
     [
       {
         "id": "123",
         "name": "Course Name",
         "level": "Beginner"
       },
       {
         "id": "124",
         "name": "Another Course",
         "level": "Intermediate"
       }
     ]
     ```
   - **Test**: Ensure that the response returns a JSON array of all course records, including name and level fields for each course.

3. **Update a Course Record**: A user can update an existing course by providing the course ID and new values for the name or level.
   - **Endpoint**: `PUT /courses/{id}`
   - **Request Body**:
     ```json
     {
       "name": "Updated Course Name",
       "level": "Advanced"
     }
     ```
   - **Response**:
     - Status Code: `200 OK`
     - Body:
     ```json
     {
       "id": "123",
       "name": "Updated Course Name",
       "level": "Advanced"
     }
     ```
   - **Test**: Ensure that updating a valid course ID successfully reflects changes in the database and maintains the integrity of existing data.

4. **Field Validation for Course**: When creating or updating a course record, the system should validate that both name and level fields are provided.
   - **Endpoint**: `POST /courses` and `PUT /courses/{id}`
   - **Response**:
     - Status Code: `400 Bad Request`
     - Body on failure:
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Name and level fields are required.",
         "details": {}
       }
     }
     ```
   - **Test**: Ensure that submitting a request without the required fields results in appropriate error responses.

## Setup and Run Instructions

1. **Clone the repository**:
   ```bash
   git clone https://your-repo-url.git
   cd course_app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn src.main:app --reload
   ```

4. **Access the API documentation** at `http://localhost:8000/docs`.

## Testing

To run the tests for the API, use the following command:
```bash
pytest tests/
```

This will ensure that all functionalities are validated and working correctly.