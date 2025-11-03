```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses using FastAPI and a SQLite database.

## Main Functions

The Teacher Management System provides the following functionalities:

- **Create and Manage Teachers**: Add new teachers with their names and email addresses.
- **Create and Manage Students**: Add new students with their names and email addresses.
- **Create and Manage Courses**: Add new courses with their names and levels.
- **Enroll Students in Courses**: Enroll students in various courses.
- **Retrieve Information**: Fetch lists of teachers, students, and courses.

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
   alembic
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migrations:
   ```bash
   alembic upgrade head
   ```

## Usage

### Running the Application

To start the FastAPI application, run the following command:
```bash
uvicorn api:router --reload
```
This will start the server at `http://127.0.0.1:8000`.

### Accessing the API

You can interact with the API using tools like Postman or cURL. Here are some example endpoints:

- **Create a Teacher**:
  ```http
  POST /teachers/
  Content-Type: application/json

  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```

- **Get All Teachers**:
  ```http
  GET /teachers/
  ```

- **Create a Student**:
  ```http
  POST /students/
  Content-Type: application/json

  {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
  }
  ```

- **Get All Students**:
  ```http
  GET /students/
  ```

- **Create a Course**:
  ```http
  POST /courses/
  Content-Type: application/json

  {
      "name": "Mathematics",
      "level": "Intermediate"
  }
  ```

- **Get All Courses**:
  ```http
  GET /courses/
  ```

- **Enroll a Student in a Course**:
  ```http
  POST /students/{student_id}/courses/{course_id}
  ```

### GUI Application

To run the GUI application, execute the following command:
```bash
python main.py
```
This will launch a Tkinter-based GUI for managing students and courses.

## Conclusion

The Teacher Management System is a straightforward application designed to help manage educational entities efficiently. By following the installation and usage instructions, you can set up and run the application with ease. For any issues or feature requests, please reach out to the development team.
```