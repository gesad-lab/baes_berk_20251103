```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create, retrieve, and manage relationships between these entities.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records, including the ability to associate courses with teachers.
- **Teacher Management**: Create and retrieve teacher records.
- **Relationships**: Establish relationships between students and courses, as well as between courses and teachers.

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
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Running the Application

1. **Start the Server**:
   Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

### API Endpoints

- **Students**:
  - `POST /students/`: Create a new student.
  - `GET /students/`: Retrieve a list of students.

- **Courses**:
  - `POST /courses/`: Create a new course (associate with a teacher using `teacher_id`).
  - `GET /courses/`: Retrieve a list of courses.

- **Teachers**:
  - `POST /teachers/`: Create a new teacher.
  - `GET /teachers/`: Retrieve a list of teachers.

### Example Usage

1. **Create a Teacher**:
   ```json
   POST /teachers/
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

2. **Create a Course**:
   ```json
   POST /courses/
   {
       "name": "Mathematics 101",
       "level": "Beginner",
       "teacher_id": 1  # Assuming the teacher ID is 1
   }
   ```

3. **Create a Student**:
   ```json
   POST /students/
   {
       "name": "Jane Smith",
       "email": "jane.smith@example.com",
       "course_ids": [1]  # Assuming the course ID is 1
   }
   ```

### Database Migration

The application includes a migration script that ensures the database schema is updated to include the new teacher relationship without losing existing data. To run the migration, execute:
```bash
python migration.py
```

## Conclusion

The ChatDev Course Management System provides a robust framework for managing educational entities. With its easy-to-use API and clear documentation, you can efficiently manage students, courses, and teachers. For further assistance, please refer to the API documentation or reach out to our support team.

Happy coding!
```