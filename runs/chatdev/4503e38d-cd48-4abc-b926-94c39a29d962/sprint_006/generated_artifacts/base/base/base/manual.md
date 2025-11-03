Here's a detailed user manual for the software, following the structure you've provided:

```markdown
# Course Management System

A simple application for managing students and courses.

## Quick Install

To set up the environment and install the necessary dependencies, run the following command:

```bash
pip install fastapi sqlalchemy alembic requests
```

Additionally, you may need to install a database driver if you are using a different database (e.g., SQLite, PostgreSQL).

## 🤔 What is this?

The Course Management System allows users to manage student and course data through a simple API. The main functionalities include:

- **Student Registration**: Add new students with their names and email addresses.
- **Course Creation**: Create new courses with a name and level.
- **Database Management**: The application uses SQLAlchemy for ORM and Alembic for database migrations.

## 📖 Main Functions

### 1. Student Registration

You can register a new student by providing their name and email address. The application will store this information in the database.

**API Endpoint**: `POST /students`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### 2. Course Creation

You can create a new course by providing its name and level. This information will be stored in the database.

**API Endpoint**: `POST /courses`

**Request Body**:
```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

## 🛠️ How to Use

1. **Run the Application**: Start the FastAPI application by running the following command in your terminal:

   ```bash
   python main.py
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

2. **Access the GUI**: You can use the provided `gui.py` script to interact with the API through a simple graphical user interface. Run it with:

   ```bash
   python gui.py
   ```

3. **Use API Endpoints**: You can also interact with the API directly using tools like Postman or curl. 

   - To register a student, send a POST request to `http://127.0.0.1:8000/students` with the appropriate JSON body.
   - To create a course, send a POST request to `http://127.0.0.1:8000/courses` with the course details.

## 📚 Documentation

For more detailed documentation, including examples and API references, please refer to the code comments and structure in the provided scripts. The main files of interest are:

- `main.py`: Entry point for the FastAPI application.
- `student.py`: API routes for student operations.
- `course.py`: API routes for course operations.
- `schemas.py`: Pydantic schemas for request and response validation.
- `models.py`: SQLAlchemy models for the application.

## 🛠️ Database Migration

The application uses Alembic for managing database migrations. To apply migrations, run:

```bash
alembic upgrade head
```

This will create the necessary tables in the database while preserving existing student data.

## 🚀 Conclusion

This Course Management System provides a simple yet effective way to manage students and courses. Feel free to explore the code and customize it to fit your needs!
```

This manual provides a comprehensive overview of the software, installation instructions, main functionalities, and usage guidelines.