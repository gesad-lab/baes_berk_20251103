# README.md

# Application Name

## Description
This application is designed to manage educators and their associated entities such as students and courses.

## Endpoints

### Health Check Endpoint
- **Method**: GET
- **Endpoint**: `/health`
- **Response**: 
  - Returns the health status of the application.
  - **Example Response**:
    ```json
    {
      "status": "healthy"
    }
    ```

### Teacher Management Endpoints

#### Create a Teacher
- **Method**: POST
- **Endpoint**: `/teachers`
- **Body**:
  - `name`: String (required)
  - `email`: String (required)
- **Response**:
  - JSON object confirming the creation of the Teacher and returning the created Teacher information.
  - **Example Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

#### Retrieve a Teacher
- **Method**: GET
- **Endpoint**: `/teachers/{teacher_id}`
- **Response**:
  - JSON object containing the Teacher's name and email based on the specified teacher ID.
  - **Example Response**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

## Usage
1. **Health Check**: To monitor the health of the application, send a GET request to the `/health` endpoint.
2. **Create Teacher**: To add a new teacher, send a POST request to `/teachers` with the required body parameters.
3. **Retrieve Teacher**: To get information about a specific teacher, send a GET request to `/teachers/{teacher_id}`.

## Testing
For testing the above functionalities, the following test cases are defined.

### Health Check Test
- Ensure the `/health` endpoint returns a 200 status code with the expected JSON response.

### Teacher Management Tests
- Test creating a teacher with valid input and verify the response.
- Test retrieving a teacher by ID and validate the returned data.

Make sure to run the tests after making any changes to the code.