# README.md

# Student Management Web Application

## Overview
The Student Management Web Application enables the management and tracking of courses and teachers. Recent enhancements have introduced a relationship between the **Course** entity and the **Teacher** entity, improving organization, oversight, and communication.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/student_management_app.git
   cd student_management_app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root based on the `.env.example` file provided.

5. **Run the application**:
   ```bash
   uvicorn src.main:app --reload
   ```

## Testing
To run the unit tests for the application, utilize the following command:

```bash
pytest tests/
```

### Unit Tests for Teacher Assignment API
Unit tests ensuring the correct functionality of the teacher assignment feature have been implemented. The tests cover successful and unsuccessful assignment attempts.

- **Successful assignment**:
    ```python
    def test_assign_teacher_to_course(client):
        response = client.post('/courses/1/assignTeacher', json={"teacherId": 1})
        assert response.status_code == 200
        assert response.json()["teacher_id"] == 1
    ```

- **Non-existent teacher assignment**:
    ```python
    def test_assign_teacher_non_existent(client):
        response = client.post('/courses/1/assignTeacher', json={"teacherId": 999})
        assert response.status_code == 404
        assert response.json()["error"]["code"] == "E001"  # Code for non-existent teacher
    ```

## Conclusion
This application aims to provide efficient tracking and management of courses and their assigned teachers, optimizing administrative operations and enhancing user experience.