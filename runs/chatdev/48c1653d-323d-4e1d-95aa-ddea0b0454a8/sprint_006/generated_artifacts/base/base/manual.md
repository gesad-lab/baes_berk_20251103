```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System, a powerful application designed to manage students and their course enrollments efficiently. This manual will guide you through the main functions of the software, how to install the necessary environment dependencies, and how to use the application effectively.

## Main Functions

The ChatDev Course Management System provides the following key functionalities:

- **Student Management**: Create, read, and manage student records, including their names and email addresses.
- **Course Management**: Create, read, and manage course records, including course names and levels.
- **Course Enrollment**: Establish a many-to-many relationship between students and courses, allowing students to enroll in multiple courses and courses to have multiple students.

## Installation

To set up the ChatDev Course Management System, follow these steps:

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
   Make sure you have Python 3.7 or higher installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can install the necessary packages individually:
   ```bash
   pip install fastapi sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**:
   To set up the database schema, run the following command:
   ```bash
   alembic upgrade head
   ```

## Usage

Once the installation is complete, you can start using the ChatDev Course Management System.

1. **Start the FastAPI Application**:
   Run the following command to start the application:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   The following API endpoints are available for interacting with the system:

   - **Create a Student**:
     - **Endpoint**: `POST /students/`
     - **Request Body**:
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

   - **Get All Students**:
     - **Endpoint**: `GET /students/`
     - **Response**: A list of all students.

   - **Create a Course**:
     - **Endpoint**: `POST /courses/`
     - **Request Body**:
       ```json
       {
         "name": "Mathematics",
         "level": "Intermediate"
       }
       ```

   - **Get All Courses**:
     - **Endpoint**: `GET /courses/`
     - **Response**: A list of all courses.

3. **Enroll a Student in a Course**:
   To enroll a student in a course, you can update the `courses` field in the `Student` entity. This can be done by modifying the student record to include the course IDs.

## Conclusion

The ChatDev Course Management System is designed to simplify the management of students and courses. With its intuitive API and robust functionality, you can efficiently handle student enrollments and course management. For further assistance, please refer to the documentation or contact our support team.

Happy coding!
```