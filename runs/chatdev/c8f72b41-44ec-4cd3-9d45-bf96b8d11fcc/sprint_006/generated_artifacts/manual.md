Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management System

A comprehensive application for managing students, courses, and teachers, enabling educational institutions to streamline their operations.

## Main Functions

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records, including assigning teachers to courses.
- **Teacher Management**: Create, retrieve, and manage teacher records.
- **Enrollment**: Enroll students in courses and manage their course selections.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student_app.git
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   ```

4. **Initialize the Database**:
   Run the following command to create the database and tables:
   ```bash
   python -m alembic upgrade head
   ```

## How to Use the Application

1. **Start the FastAPI Server**:
   Run the following command to start the application:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Managing Students**:
   - **Create a Student**:
     - Endpoint: `POST /students/`
     - Body: 
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

   - **Get All Students**:
     - Endpoint: `GET /students/`

4. **Managing Courses**:
   - **Create a Course**:
     - Endpoint: `POST /courses/`
     - Body:
       ```json
       {
         "name": "Mathematics",
         "level": "Intermediate",
         "teacher_id": 1  // Optional, if a teacher is assigned
       }
       ```

   - **Get All Courses**:
     - Endpoint: `GET /courses/`

5. **Managing Teachers**:
   - **Create a Teacher**:
     - Endpoint: `POST /teachers/`
     - Body:
       ```json
       {
         "name": "Jane Smith",
         "email": "jane.smith@example.com"
       }
       ```

   - **Get All Teachers**:
     - Endpoint: `GET /teachers/`

6. **Enroll Students in Courses**:
   - **Add Courses to a Student**:
     - Endpoint: `PUT /students/{student_id}/courses/`
     - Body:
       ```json
       {
         "course_ids": [1, 2, 3]  // List of course IDs to enroll
       }
       ```

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is located at `./students.db`.
- **Database Migration**: The application uses Alembic for database migrations. Ensure to run migrations whenever you make changes to the database schema.
- **Testing**: You can write unit tests to ensure the functionality of the application. Use a testing framework like `pytest`.

For further details, please refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/) and [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/).

```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines. Let me know if you need any modifications or additional information!