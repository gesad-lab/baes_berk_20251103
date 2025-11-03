```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses in an educational environment.

## Main Functions

This software provides the following main functionalities:

- **Create and manage Teachers**: Add new teachers with their names and email addresses.
- **Create and manage Students**: Add new students with their names and email addresses.
- **Create and manage Courses**: Add new courses with their names and levels.
- **Enroll Students in Courses**: Enroll students in specific courses.
- **Retrieve lists of Teachers, Students, and Courses**: Fetch all teachers, students, or courses from the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
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

1. **Initialize the database**:
   Run the following command to create the database and tables:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

2. **Run migrations**:
   To apply the latest database migrations, use Alembic:
   ```bash
   alembic upgrade head
   ```

## Usage

1. **Start the API server**:
   Use Uvicorn to run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   The API will be available at `http://127.0.0.1:8000`. You can use tools like Postman or curl to interact with the API.

### API Endpoints

- **Create a Teacher**:
   - **Endpoint**: `POST /teachers/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

- **Retrieve all Teachers**:
   - **Endpoint**: `GET /teachers/`
   - **Response**:
     ```json
     [
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
     ]
     ```

- **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "Jane Smith",
       "email": "jane.smith@example.com"
     }
     ```

- **Retrieve all Students**:
   - **Endpoint**: `GET /students/`
   - **Response**:
     ```json
     [
       {
         "id": 1,
         "name": "Jane Smith",
         "email": "jane.smith@example.com"
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

- **Enroll a Student in a Course**:
   - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
   - **Response**:
     ```json
     {
       "message": "Student enrolled in course successfully."
     }
     ```

## Conclusion

This Teacher Management System provides a simple yet effective way to manage educational entities. By following the installation and usage instructions, you can set up and run the API to manage teachers, students, and courses efficiently.
```