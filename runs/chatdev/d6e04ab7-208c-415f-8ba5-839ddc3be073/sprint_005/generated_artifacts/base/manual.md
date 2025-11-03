Here's a detailed user manual for the software that incorporates the new course relationship functionality between the Student and Course entities.

```markdown
# Student Course Management Application

A FastAPI application for managing students and their enrolled courses.

## Main Functions

This application allows users to:

- Create and manage student records.
- Create and manage course records.
- Enroll students in multiple courses.
- Retrieve lists of students and courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi[all] sqlalchemy alembic
   ```

## Database Setup

The application uses SQLite as the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

### Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

#### 1. Create a Student

**Endpoint:** `POST /students/`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "course_ids": [1, 2]  // Optional: List of course IDs to enroll the student in
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

#### 2. Retrieve Students

**Endpoint:** `GET /students/`

**Query Parameters:**
- `skip`: Number of records to skip (for pagination).
- `limit`: Number of records to return.

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
]
```

#### 3. Create a Course

**Endpoint:** `POST /courses/`

**Request Body:**
```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Beginner"
}
```

#### 4. Retrieve Courses

**Endpoint:** `GET /courses/`

**Query Parameters:**
- `skip`: Number of records to skip (for pagination).
- `limit`: Number of records to return.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Mathematics",
    "level": "Beginner"
  }
]
```

## Database Migration

To apply database migrations, you can use Alembic. Ensure you have the migration script set up correctly and run the following command:

```bash
alembic upgrade head
```

This will create the necessary tables and relationships in the database while preserving existing data.

## Conclusion

This application provides a simple yet effective way to manage students and their courses. For further customization and enhancements, feel free to modify the code as needed.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, installation instructions, usage details, and API endpoints, ensuring that users can effectively utilize the software.