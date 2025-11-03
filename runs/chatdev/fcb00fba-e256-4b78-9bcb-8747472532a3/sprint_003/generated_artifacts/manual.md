```markdown
# Course Management System

A web application for managing students and courses, allowing users to create and retrieve student and course data.

## Main Functions

- **Create Student**: Allows users to add new students to the database with their name and email.
- **Retrieve Students**: Fetches a list of students from the database with pagination support.
- **Create Course**: Enables users to add new courses with a name and level.
- **Retrieve Courses**: Fetches a list of courses from the database with pagination support.

## Installation

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/course-management-system.git
cd course-management-system
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install fastapi sqlalchemy pydantic alembic uvicorn
```

### Step 4: Run Database Migrations

Before running the application, ensure that the database schema is up to date. Run the Alembic migration script:

```bash
alembic upgrade head
```

### Step 5: Start the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## Usage

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Students

To retrieve a list of students, send a GET request to `/students/`. You can use query parameters `skip` and `limit` for pagination:

```
GET /students/?skip=0&limit=10
```

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Retrieving Courses

To retrieve a list of courses, send a GET request to `/courses/`. Similar to students, you can use query parameters `skip` and `limit` for pagination:

```
GET /courses/?skip=0&limit=10
```

## Documentation

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Support

If you encounter any issues or have questions, please reach out through our support channels or open an issue in the repository.

```
