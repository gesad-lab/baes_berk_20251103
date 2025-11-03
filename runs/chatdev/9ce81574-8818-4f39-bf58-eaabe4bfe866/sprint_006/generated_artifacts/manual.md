```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create, retrieve, and manage relationships between these entities seamlessly.

## Main Functions

- **Student Management**: Create and manage student records, including their enrollment in courses.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher records and their associated courses.
- **Enrollment**: Enroll students in courses and manage their course registrations.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Starting the Application

1. **Run the FastAPI Application**:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

You can interact with the application using the following API endpoints:

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip`, `limit`

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Optional Parameter**: `teacher_id` (to assign a teacher)

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Path Parameters**: `student_id`, `course_id`

### Database Migration

To apply database migrations, use Alembic. Ensure you have the migration script ready and run:
```bash
alembic upgrade head
```
This will update the database schema while preserving existing data.

## Documentation

For more detailed documentation, please refer to the following sections:

- **Getting Started**: Installation, setting up the environment, and simple examples.
- **How-To Examples**: Demos, integrations, and helper functions.
- **Reference**: Full API documentation.
- **Resources**: High-level explanations of core concepts.

For any issues or support, please reach out to our support team.

Happy coding!
```