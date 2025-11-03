```markdown
# Course Management API

A FastAPI application for managing students and courses, allowing users to create and retrieve student and course records.

## Main Functions

This software provides the following functionalities:

- **Create Student**: Allows users to add new students with their names and email addresses.
- **Get Students**: Retrieves a list of existing students with pagination support.
- **Create Course**: Enables users to create new courses with a name and level.
- **Get Courses**: Fetches a list of existing courses with pagination support.

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
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. **Initialize the Database**:
   The application uses SQLite for the database. The database schema will be created automatically when the application starts.

2. **Run Migrations**:
   To add the Course table to the database, run the following command:
   ```bash
   alembic upgrade head
   ```

## Usage

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   The API will be available at `http://127.0.0.1:8000`. You can use tools like Postman or cURL to interact with the API.

### API Endpoints

- **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**: Returns the created student object.

- **Get Students**:
   - **Endpoint**: `GET /students/`
   - **Query Parameters**: `skip` (int), `limit` (int)
   - **Response**: Returns a list of students.

- **Create a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```
   - **Response**: Returns the created course object.

- **Get Courses**:
   - **Endpoint**: `GET /courses/`
   - **Query Parameters**: `skip` (int), `limit` (int)
   - **Response**: Returns a list of courses.

## Conclusion

This Course Management API provides a simple yet effective way to manage students and courses. With the ability to create and retrieve records, it serves as a foundational tool for educational applications. For further customization and enhancements, feel free to modify the codebase as per your requirements.
```