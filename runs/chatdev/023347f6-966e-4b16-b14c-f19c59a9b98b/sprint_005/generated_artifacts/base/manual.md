```markdown
# Student-Course Management System

A simple application for managing students and their associated courses. This system allows users to create students, create courses, and associate students with multiple courses.

## Main Functions

- **Create Student**: Add a new student with a name, email, and associated courses.
- **Get Students**: Retrieve a list of all students along with their associated courses.
- **Create Course**: Add a new course with a name and level.
- **Get Courses**: Retrieve a list of all available courses.

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
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

The application uses SQLite for the database. The database schema will be created automatically when you run the application for the first time.

1. **Run the Migration Script**:
   To create the necessary tables in the database, execute the following command:
   ```bash
   python main.py
   ```

## Usage

### Running the Application

To start the FastAPI application, use the following command:
```bash
uvicorn routes:student_router --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]  // List of course IDs to associate with the student
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "course_ids": [1, 2]
      }
    ]
    ```

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

## Conclusion

This Student-Course Management System provides a straightforward way to manage students and their courses. By following the installation and usage instructions, you can set up and run the application locally. For further enhancements or features, feel free to modify the code as per your requirements.
```