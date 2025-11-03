Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Course Management System

A comprehensive application for managing students and their course enrollments. This system allows users to create students, create courses, and enroll students in courses, all while maintaining a robust database structure.

## Main Functions

- **Create Student**: Add a new student with their name and email.
- **Read Student**: Retrieve information about a specific student, including their enrolled courses.
- **Create Course**: Add a new course with its name and level.
- **Read Course**: Retrieve information about a specific course.
- **Enroll Student in Course**: Enroll a student in a specific course, establishing a many-to-many relationship between students and courses.

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
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Initialize the Database**:
   Run the following command to create the initial database schema:
   ```bash
   python main.py
   ```

5. **Run Database Migrations**:
   To apply any migrations, run:
   ```bash
   alembic upgrade head
   ```

## Usage

Once the application is running, you can interact with it through HTTP requests. Below are examples of how to use the main functionalities.

### Create a Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Read a Student

**Endpoint**: `GET /students/{student_id}`

**Example**: `GET /students/1`

### Create a Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
  "name": "Mathematics",
  "level": "Intermediate"
}
```

### Read a Course

**Endpoint**: `GET /courses/{course_id}`

**Example**: `GET /courses/1`

### Enroll a Student in a Course

**Endpoint**: `POST /students/{student_id}/enroll/{course_id}`

**Example**: `POST /students/1/enroll/1`

### Example of Using cURL

You can use cURL to interact with the API. Here’s an example of creating a student:

```bash
curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
```

## Documentation

For more detailed documentation, including API reference and examples, please refer to the code comments and the FastAPI documentation [here](https://fastapi.tiangolo.com).

## Support

If you encounter any issues or have questions, please reach out to our support team via the designated support channel.
```

This manual provides a comprehensive overview of the software's capabilities, installation steps, and usage instructions, ensuring that users can effectively utilize the Student Course Management System.