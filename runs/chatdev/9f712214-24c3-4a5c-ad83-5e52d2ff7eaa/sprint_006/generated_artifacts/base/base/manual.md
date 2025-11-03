```markdown
# Student Management System

A simple application for managing students and courses, allowing users to create students, create courses, and enroll students in courses.

## Main Functions

- **Create Student**: Allows users to add new students to the database.
- **Create Course**: Enables users to create new courses.
- **Enroll Student in Course**: Facilitates the enrollment of students in specific courses.
- **View Students**: Retrieve a list of all students in the database.
- **View Courses**: Retrieve a list of all courses in the database.

## Installation

To set up the environment and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi sqlalchemy alembic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration scripts:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Access the GUI**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

2. **Creating a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Submit" button to create the student. A confirmation message will appear if successful.

3. **Creating a Course**:
   - Enter the course name and level in the respective fields.
   - Click the "Submit" button to create the course. A confirmation message will appear if successful.

4. **Enrolling a Student in a Course**:
   - Use the API endpoint `/students/{student_id}/courses/{course_id}` to enroll a student in a course. You can use tools like Postman or cURL to make this request.

5. **Viewing Students and Courses**:
   - You can retrieve a list of students and courses by accessing the respective API endpoints:
     - `/students/` for students
     - `/courses/` for courses

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database file is created in the project directory.
- **API Documentation**: You can access the automatically generated API documentation by navigating to `http://127.0.0.1:8000/docs`.

## Support

For any issues or questions, please reach out to the development team via the support channel.

```
