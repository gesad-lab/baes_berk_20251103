# README.md

# Course Enrollment System

This repository is designed to manage a course enrollment system allowing students to enroll in courses, retrieve course information, and remove courses as needed.

## Project Overview

The project is structured to include separate modules for different functionalities, enhancing maintainability and scalability. 

## Week-by-Week Milestones

- **Week 1**: Define new models (`Course`, `StudentCourse`) and update module structure.
- **Week 2**: Implement endpoints for enrolling, retrieving, and removing courses for students.
- **Week 3**: Develop and run tests to ensure functionality and coverage.
- **Week 4**: Code review, finalize documentation, and prepare for deployment.

## Installation

To set up the environment for this project, follow these steps:

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   It is recommended to use a virtual environment for Python:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   Ensure that your database is up to date:
   ```
   python manage.py migrate
   ```

## Usage

### API Endpoints

- **Enroll a Student in a Course**: 
    - **URL**: `/students/enroll`
    - **Method**: `POST`
    - **Request Body**:
      ```json
      {
          "student_id": 1,
          "course_id": 1
      }
      ```
    - **Response**: 
      ```json
      {
          "status": "success",
          "data": {
              "courses": [1, 2, 3]
          }
      }
      ```

- **Retrieve Enrolled Courses**: 
    - **URL**: `/students/courses`
    - **Method**: `GET`
    - **Response** Example: 
    ```json
    {
        "status": "success",
        "data": {
            "courses": [1, 2]
        }
    }
    ```

- **Remove a Course from a Student**: 
    - **URL**: `/students/remove`
    - **Method**: `DELETE`
    - **Request Body**:
      ```json
      {
          "student_id": 1,
          "course_id": 1
      }
      ```
    - **Response**: 
      ```json
      {
          "status": "success",
          "message": "Course removed successfully."
      }
      ```

## Testing

Tests confirm that the implemented functionalities work as expected. Utilize the following command to run the tests:

```bash
pytest -v
```

**Example test case**:
```python
def test_enroll_student_in_course(student_service):
    response = client.post("/students/enroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert "courses" in response.json()["data"]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to all contributors and open-source libraries that made this project successful.

For additional details, please refer to the technical documentation or contact the project maintainers.

--- 

This README provides a comprehensive overview of the project setup, usage, and testing, adhering to the required guidelines and documentation standards.