Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational environment.

## Main Functions

The Teacher Management System provides the following functionalities:

- **Create a Teacher**: Add a new teacher with a name and email.
- **Retrieve Teachers**: Get a list of all teachers in the system.
- **Create a Student**: Add a new student with a name, email, and associated courses.
- **Retrieve Students**: Get a list of all students in the system.
- **Create a Course**: Add a new course with a name and level.
- **Retrieve Courses**: Get a list of all courses in the system.

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
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

4. **Database Setup**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API**:
   You can interact with the API using tools like Postman or cURL. The API documentation is available at `http://127.0.0.1:8000/docs`.

3. **API Endpoints**:
   - **Create a Teacher**:
     - **Endpoint**: `POST /teachers/`
     - **Request Body**:
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
   - **Get Teachers**:
     - **Endpoint**: `GET /teachers/`
     - **Response**: Returns a list of teachers.

   - **Create a Student**:
     - **Endpoint**: `POST /students/`
     - **Request Body**:
       ```json
       {
         "name": "Jane Smith",
         "email": "jane.smith@example.com",
         "course_ids": [1, 2]
       }
       ```

   - **Get Students**:
     - **Endpoint**: `GET /students/`
     - **Response**: Returns a list of students.

   - **Create a Course**:
     - **Endpoint**: `POST /courses/`
     - **Request Body**:
       ```json
       {
         "name": "Mathematics",
         "level": "Intermediate"
       }
       ```

   - **Get Courses**:
     - **Endpoint**: `GET /courses/`
     - **Response**: Returns a list of courses.

## Conclusion

The Teacher Management System is designed to simplify the management of teachers, students, and courses in educational institutions. By following the installation and usage instructions, you can quickly set up and start using the API.

For further assistance, please refer to the API documentation or contact support.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, and usage guidelines.