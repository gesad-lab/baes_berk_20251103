Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses in an educational environment.

## Main Functions

This application allows users to perform the following key functions:

- **Create Teachers**: Add new teachers to the system with their name and email.
- **Create Students**: Add new students to the system with their name, email, and associated courses.
- **Create Courses**: Add new courses to the system with their name and level.
- **Data Persistence**: All data is stored in a SQLite database, ensuring that information is preserved across sessions.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

Once the application is running, you can interact with it through the following API endpoints:

### 1. Create a Teacher

- **Endpoint**: `POST /teachers/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

### 2. Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "course_ids": [1, 2]  // Optional: List of course IDs to associate with the student
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "courses": []  // List of courses associated with the student
  }
  ```

### 3. Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```

## Database Migration

The application includes a migration function that ensures the database schema is updated to include the new Teacher table while preserving existing Student and Course data. This is automatically handled during the application startup.

## Conclusion

This Teacher Management System provides a straightforward interface for managing educational entities. For further details or support, please refer to the code documentation or contact the development team.
```

This manual provides a comprehensive overview of the software, including installation steps and usage instructions for the key functionalities.