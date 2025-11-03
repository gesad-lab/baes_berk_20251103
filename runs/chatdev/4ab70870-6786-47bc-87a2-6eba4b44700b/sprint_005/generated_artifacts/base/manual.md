```markdown
# Student Course Management System

A FastAPI application for managing students and their courses, allowing for easy creation and retrieval of student and course records.

## Main Functions

- **Create Students**: Add new students to the database with their name and email.
- **Retrieve Students**: Fetch a list of students from the database.
- **Create Courses**: Add new courses to the database with their name and level.
- **Retrieve Courses**: Fetch a list of courses from the database.
- **Manage Relationships**: Students can be associated with multiple courses, and courses can have multiple students.

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

### Running the Application

1. **Start the FastAPI Server**:
   Use Uvicorn to run the application:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

### API Endpoints

- **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**: Returns the created student object.

- **Retrieve Students**:
   - **Endpoint**: `GET /students/`
   - **Query Parameters**: `skip` (optional), `limit` (optional)
   - **Response**: Returns a list of students.

- **Create a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Intermediate"
     }
     ```
   - **Response**: Returns the created course object.

- **Retrieve Courses**:
   - **Endpoint**: `GET /courses/`
   - **Query Parameters**: `skip` (optional), `limit` (optional)
   - **Response**: Returns a list of courses.

### Managing Relationships

To associate students with courses, you can modify the `Student` and `Course` models to include methods for adding and removing courses from a student. This can be done through additional API endpoints that handle these operations.

## Database Migration

The application uses Alembic for database migrations. To apply migrations, run:
```bash
alembic upgrade head
```

This will create the necessary tables and relationships in the database while preserving existing data.

## Conclusion

This Student Course Management System provides a robust framework for managing students and their courses. With FastAPI's performance and ease of use, you can quickly build and scale your application to meet your needs.
```
