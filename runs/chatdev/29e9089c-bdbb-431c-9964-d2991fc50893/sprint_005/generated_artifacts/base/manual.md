```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students and their course enrollments effectively. Below is a detailed user manual to help you understand the main functions of the software, how to install the necessary environment dependencies, and how to use the application.

## Main Functions

The ChatDev Course Management System provides the following main functionalities:

1. **Student Management**: 
   - Create new students with their names and email addresses.
   - Retrieve a list of all students.

2. **Course Management**: 
   - Create new courses with their names and levels.
   - Retrieve a list of all courses.

3. **Enrollment Management**: 
   - Enroll students in courses.
   - Retrieve the list of courses a specific student is enrolled in.

## Installation of Environment Dependencies

To run the ChatDev Course Management System, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
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
   The application will be available at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Create a Student**:
   Send a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Create a Course**:
   Send a POST request to `/courses/` with the following JSON body:
   ```json
   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```

5. **Enroll a Student in a Course**:
   Send a POST request to `/students/{student_id}/courses/{course_id}` where `{student_id}` and `{course_id}` are the IDs of the student and course respectively.

6. **Get Student Courses**:
   Send a GET request to `/students/{student_id}/courses/` to retrieve the list of courses a specific student is enrolled in.

## Conclusion

The ChatDev Course Management System is designed to streamline the management of students and their course enrollments. With the provided API, you can easily create, retrieve, and manage student and course data. For further assistance, please refer to the API documentation or contact our support team.

Happy coding!
```