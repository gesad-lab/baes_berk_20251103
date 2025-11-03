```markdown
# Student Course Management System

A FastAPI application for managing students and their enrolled courses.

## Main Functions

This application allows users to perform the following functions:

- **Create Students**: Add new students to the database, including their name, email, and enrolled courses.
- **Retrieve Students**: Fetch a list of students with their details and enrolled courses.
- **Create Courses**: Add new courses to the database, specifying the course name and level.
- **Retrieve Courses**: Fetch a list of available courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## How to Use the Application

### API Endpoints

The application exposes several API endpoints for interacting with students and courses.

#### Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "course_ids": [1, 2]  // Optional: List of course IDs to enroll the student in
  }
  ```

- **Response**: Returns the created student object with their enrolled courses.

#### Retrieve Students

- **Endpoint**: `GET /students/`
- **Query Parameters**: 
  - `skip`: Number of records to skip (for pagination).
  - `limit`: Number of records to return (default is 10).

- **Response**: Returns a list of students with their details and enrolled courses.

#### Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```

- **Response**: Returns the created course object.

#### Retrieve Courses

- **Endpoint**: `GET /courses/`
- **Query Parameters**: 
  - `skip`: Number of records to skip (for pagination).
  - `limit`: Number of records to return (default is 10).

- **Response**: Returns a list of available courses.

## Database Migration

The application uses SQLAlchemy to manage the database schema. The migration script ensures that the existing Student and Course data is preserved while adding a many-to-many relationship between Students and Courses.

### Database Structure

- **Students Table**: Contains student details.
- **Courses Table**: Contains course details.
- **Student_Courses Association Table**: Manages the many-to-many relationship between students and courses.

## Conclusion

This Student Course Management System provides a simple yet effective way to manage students and their courses. For further assistance, please refer to the code documentation or reach out to the support team.
```