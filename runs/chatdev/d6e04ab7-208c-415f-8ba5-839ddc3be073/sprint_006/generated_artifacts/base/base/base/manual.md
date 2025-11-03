```markdown
# Course Management Application

This application allows users to manage courses and students through a RESTful API built with FastAPI and SQLAlchemy. Users can create and retrieve both student and course entities.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Retrieve Students**: Get a list of all students with pagination support.
- **Create Course**: Add a new course with a name and level.
- **Retrieve Courses**: Get a list of all courses with pagination support.

## Installation of Environment Dependencies

To set up the environment for this application, you need to install the required dependencies listed in the `requirements.txt` file. Follow these steps:

1. **Clone the Repository** (if applicable):
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
   You can install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI application by running the following command:
   ```bash
   python main.py
   ```
   The application will be available at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   FastAPI automatically generates interactive API documentation. You can access it by navigating to:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

3. **Creating a Student**:
   To create a new student, send a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Retrieving Students**:
   To retrieve a list of students, send a GET request to `/students/`. You can also use query parameters `skip` and `limit` for pagination:
   ```
   GET /students/?skip=0&limit=10
   ```

5. **Creating a Course**:
   To create a new course, send a POST request to `/courses/` with the following JSON body:
   ```json
   {
       "name": "Introduction to Programming",
       "level": "Beginner"
   }
   ```

6. **Retrieving Courses**:
   To retrieve a list of courses, send a GET request to `/courses/`. Similar to students, you can use `skip` and `limit` for pagination:
   ```
   GET /courses/?skip=0&limit=10
   ```

## Database Migration

The application uses Alembic for database migrations. To add the Course table to the database while preserving existing Student data, ensure you run the migration script after setting up the database.

1. **Run Migration**:
   Execute the migration script to create the Course table:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This application provides a simple yet effective way to manage students and courses through a RESTful API. For further customization or enhancements, feel free to modify the code as needed.

For any issues or support, please reach out to the development team.
```