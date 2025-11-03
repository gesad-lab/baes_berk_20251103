# docs/api_documentation.md

## API Documentation

### Base URL
```
http://api.example.com/v1
```

### Endpoints

#### 1. Assign a Teacher to a Course
- **URL**: `/courses/<course_id>`
- **Method**: `PUT`
- **Request**:
  - **Headers**: 
    - `Content-Type: application/json`
  - **Body**:
    ```json
    {
      "teacher_id": "<teacher_id>"
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "message": "Teacher successfully assigned to the course."
    }
    ```
- **Error Responses**:
  - **404 Not Found**: 
    - If the Course does not exist.
    - **Body**:
      ```json
      {
        "error": {
          "code": "E404",
          "message": "Course not found." 
        }
      }
      ```

#### 2. Retrieve Course with Teacher Information
- **URL**: `/courses/<course_id>`
- **Method**: `GET`
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "course_id": "<course_id>",
      "course_name": "<course_name>",
      "teacher": {
        "teacher_id": "<teacher_id>",
        "name": "<teacher_name>"
      }
    }
    ```

#### 3. Validate Course Updates
- **Error Responses**:
  - **404 Not Found**:
    - If the Course does not exist when attempting to assign a Teacher.
    - **Body**:
      ```json
      {
        "error": {
          "code": "E404",
          "message": "Course not found." 
        }
      }
      ```

#### 4. Multiple Courses for a Teacher
- **URL**: `/teachers/<teacher_id>/courses`
- **Method**: `GET`
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "teacher_id": "<teacher_id>",
      "courses": [
        {
          "course_id": "<course_id_1>",
          "course_name": "<course_name_1>"
        },
        {
          "course_id": "<course_id_2>",
          "course_name": "<course_name_2>"
        }
      ]
    }
    ```

### Notes
- Ensure to provide valid `course_id` and `teacher_id` as specified.
- All responses are in JSON format with appropriate error handling included.