```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers, built using FastAPI and SQLAlchemy.

## Main Functions

The Student Management Application provides the following functionalities:

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records, including assigning teachers to courses.
- **Teacher Management**: Create and retrieve teacher records.
- **Enrollment**: Enroll students in courses.
- **API Endpoints**: Interact with the application through RESTful API endpoints.

## Installation

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
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Create the Database and Apply Migrations**:
   Before running the application, ensure the database is created and migrations are applied:
   ```bash
   python main.py
   ```

2. **Start the FastAPI Server**:
   In a separate terminal, run the following command to start the FastAPI server:
   ```bash
   uvicorn api:router --reload
   ```

3. **Access the API Documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

### Interacting with the Application

- **Creating a Student**:
   Send a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

- **Creating a Teacher**:
   Send a POST request to `/teachers/` with the following JSON body:
   ```json
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
   }
   ```

- **Creating a Course**:
   Send a POST request to `/courses/` with the following JSON body (optionally including `teacher_id`):
   ```json
   {
       "name": "Mathematics",
       "level": "Beginner",
       "teacher_id": 1  // Optional
   }
   ```

- **Enrolling a Student in a Course**:
   Send a POST request to `/students/{student_id}/courses/{course_id}` to enroll a student in a course.

### GUI Usage

1. **Run the GUI**:
   After setting up the database, run the following command to start the GUI:
   ```bash
   python main.py
   ```

2. **Using the GUI**:
   - The GUI will provide options to manage students, teachers, and courses.
   - Follow the on-screen instructions to create and manage records.

## Conclusion

The Student Management Application is designed to streamline the management of educational entities. With its intuitive API and GUI, users can efficiently handle student, teacher, and course data. For further assistance, please refer to the API documentation or contact support.
```