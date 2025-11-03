```markdown
# Course Management Application

A simple application for managing students and courses, built using FastAPI and SQLAlchemy.

## Main Functions

The Course Management Application allows users to perform the following functions:

- **Create Students**: Add new students to the database with their name and email.
- **Create Courses**: Add new courses with a name and level.
- **Database Management**: The application uses SQLAlchemy for ORM and Alembic for database migrations, ensuring that existing student data is preserved during updates.

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
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be available at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by Swagger UI.

3. **Create a Student**:
   To add a new student, send a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Create a Course**:
   To add a new course, send a POST request to `/courses/` with the following JSON body:
   ```json
   {
       "name": "Introduction to Programming",
       "level": "Beginner"
   }
   ```

## Database Migration

The application uses Alembic for managing database migrations. To apply migrations, run the following command:
```bash
alembic upgrade head
```
This will create the necessary tables in the database, including the `students` and `courses` tables.

## Conclusion

This Course Management Application provides a simple interface for managing students and courses. With the power of FastAPI and SQLAlchemy, it is designed to be efficient and easy to use. For further customization or features, feel free to modify the code as needed.
```
