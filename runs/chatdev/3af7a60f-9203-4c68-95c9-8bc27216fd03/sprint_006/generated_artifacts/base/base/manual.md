```markdown
# Student and Course Management Application

This application allows users to manage students and their associated courses through a simple GUI and a RESTful API. Users can create students, enroll them in courses, and manage course information.

## Main Functions

- **Create Student**: Add a new student with a name, email, and a list of course IDs they are enrolled in.
- **Get Students**: Retrieve a list of all students with their details.
- **Create Course**: Add a new course with a name and level.
- **Get Courses**: Retrieve a list of all courses available in the system.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Run the following command to create the initial database schema:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

5. **Run Database Migrations**:
   If you have Alembic set up, run the migration script:
   ```bash
   alembic upgrade head
   ```

6. **Start the Application**:
   Use Uvicorn to run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### GUI Usage

1. **Launch the Application**:
   Run the `main.py` file:
   ```bash
   python main.py
   ```

2. **Adding a Student**:
   - Enter the student's name and email.
   - Enter the course IDs they should be enrolled in (comma-separated).
   - Click the "Submit Student" button to add the student.

3. **Adding a Course**:
   - Enter the course name and level.
   - Click the "Submit Course" button to add the course.

4. **Viewing Results**:
   - After submitting, the application will display a success message or an error message based on the operation's outcome.

### API Usage

You can also interact with the application using the RESTful API. Here are some example requests:

- **Create a Student**:
   ```bash
   POST /students/
   {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "courses": [1, 2]
   }
   ```

- **Get Students**:
   ```bash
   GET /students/
   ```

- **Create a Course**:
   ```bash
   POST /courses/
   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```

- **Get Courses**:
   ```bash
   GET /courses/
   ```

## Conclusion

This application provides a straightforward way to manage students and courses. Whether you prefer using the GUI or the API, you can easily add, retrieve, and manage your data. For any issues or feature requests, please reach out to the development team.
```