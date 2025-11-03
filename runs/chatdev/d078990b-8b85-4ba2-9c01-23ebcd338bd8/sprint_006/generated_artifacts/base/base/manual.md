```markdown
# ChatDev Student-Course Management System

Welcome to the ChatDev Student-Course Management System! This software allows you to manage students and their course enrollments effectively. 

## Main Functions

- **Create Students**: Add new students to the system with their names, emails, and enrolled courses.
- **Retrieve Students**: Fetch a list of students along with their enrolled courses.
- **Create Courses**: Add new courses with specific names and levels.
- **Retrieve Courses**: Fetch a list of available courses and their enrolled students.

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
   ```plaintext
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

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   - **Create a Student**:
     - **Endpoint**: `POST /students/`
     - **Request Body**:
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com",
         "course_ids": [1, 2]  // List of course IDs to enroll in
       }
       ```
     - **Response**: Returns the created student object.

   - **Retrieve Students**:
     - **Endpoint**: `GET /students/`
     - **Response**: Returns a list of students with their details and enrolled courses.

   - **Create a Course**:
     - **Endpoint**: `POST /courses/`
     - **Request Body**:
       ```json
       {
         "name": "Mathematics",
         "level": "Beginner"
       }
       ```
     - **Response**: Returns the created course object.

   - **Retrieve Courses**:
     - **Endpoint**: `GET /courses/`
     - **Response**: Returns a list of courses with their details and enrolled students.

## Database Migration

The application uses Alembic for database migrations. When you first run the application, it will check if the database exists and apply any necessary migrations to ensure that the schema is up-to-date while preserving existing data.

## Conclusion

This system provides a robust solution for managing students and their course enrollments. For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to their respective official documentation.

Happy coding!
```