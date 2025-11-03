```markdown
# Course Management Application

A simple application for managing students and courses using FastAPI and SQLAlchemy.

## Main Functions

This application provides the following functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically manage database schema changes while preserving existing data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The application requires the following Python packages:

- **fastapi**: The web framework used to create the API.
- **uvicorn**: The ASGI server for running the FastAPI application.
- **sqlalchemy**: The ORM used for database interactions.
- **alembic**: The migration tool for managing database schema changes.
- **pydantic**: Used for data validation and serialization with FastAPI.

Make sure to adjust the version numbers in `requirements.txt` as needed based on your project's requirements or compatibility.

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Creating a Student**:
   - Send a POST request to `/students/` with a JSON body containing the student's name and email.
   - Example:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

4. **Retrieving Students**:
   - Send a GET request to `/students/` to retrieve a list of students.

5. **Creating a Course**:
   - Send a POST request to `/courses/` with a JSON body containing the course name and level.
   - Example:
     ```json
     {
       "name": "Introduction to Programming",
       "level": "Beginner"
     }
     ```

6. **Retrieving Courses**:
   - Send a GET request to `/courses/` to retrieve a list of courses.

## Database Migration

To apply the database migrations and create the Course table while preserving existing Student data, run the following command:
```bash
alembic upgrade head
```

This command will create the necessary tables in the database without affecting the existing Student records.

## Conclusion

This application serves as a foundational system for managing students and courses. You can extend its functionality by adding more features as needed. For further assistance, please refer to the FastAPI documentation or reach out to the development team.

Happy coding!
```