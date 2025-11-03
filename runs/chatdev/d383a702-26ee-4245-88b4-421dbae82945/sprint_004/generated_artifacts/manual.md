```markdown
# ChatDev Student-Course Management System

Welcome to the ChatDev Student-Course Management System! This software allows you to manage students and their associated courses efficiently. Below, you will find a detailed user manual that covers the main functions of the software, installation instructions, and usage guidelines.

## Main Functions

The ChatDev system provides the following functionalities:

1. **Student Management**:
   - Create new students with their names and email addresses.
   - Retrieve a list of all students.

2. **Course Management**:
   - Create new courses with their names and levels.
   - Retrieve a list of all courses.

3. **Course Enrollment**:
   - Enroll students in courses.
   - Check if a student is already enrolled in a specific course.

## Quick Install

To get started with the ChatDev system, you need to install the required dependencies. You can do this using `pip` or `conda`.

### Using pip

```bash
pip install -r requirements.txt
```

### Using conda

```bash
conda install --file requirements.txt
```

## Environment Setup

1. **Clone the Repository**:
   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Follow the Quick Install instructions above to install the necessary dependencies.

3. **Database Initialization**:
   The application uses SQLite as the database. The database will be automatically created when you run the application for the first time.

## How to Use the Application

### Starting the Application

To start the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This command will run the application in development mode, allowing you to see changes without restarting the server.

### API Endpoints

The application exposes several API endpoints for managing students and courses. Below are the key endpoints:

1. **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**: Returns the created student object.

2. **Retrieve Students**:
   - **Endpoint**: `GET /students/`
   - **Response**: Returns a list of all students.

3. **Create a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```
   - **Response**: Returns the created course object.

4. **Retrieve Courses**:
   - **Endpoint**: `GET /courses/`
   - **Response**: Returns a list of all courses.

5. **Enroll a Student in a Course**:
   - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
   - **Response**: Returns the updated student object with the associated courses.

### Example Usage

1. **Creating a Student**:
   Send a `POST` request to `/students/` with the student details.

2. **Creating a Course**:
   Send a `POST` request to `/courses/` with the course details.

3. **Enrolling a Student**:
   Send a `POST` request to `/students/{student_id}/courses/{course_id}` to enroll a student in a course.

4. **Retrieving Students and Courses**:
   Send a `GET` request to `/students/` or `/courses/` to retrieve the lists.

## Conclusion

The ChatDev Student-Course Management System is designed to simplify the management of students and courses. By following the instructions in this manual, you should be able to set up the environment and start using the application effectively. For any further assistance, please refer to the documentation or contact support.

Happy coding!
```