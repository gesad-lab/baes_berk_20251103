```markdown
# ChatDev Student-Course Management System

Welcome to the ChatDev Student-Course Management System! This software allows you to manage students and their course enrollments efficiently.

## Main Functions

- **Student Management**: Create, read, and manage student records, including their names and email addresses.
- **Course Management**: Create, read, and manage courses, including course names and levels.
- **Enrollment**: Enroll students in courses and manage their course relationships.

## Quick Install

To get started, you'll need to install the required dependencies. You can do this using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, if you prefer using `conda`, you can install the dependencies as follows:

```bash
conda install fastapi uvicorn sqlalchemy pydantic alembic -c conda-forge
```

## Getting Started

### Setting Up the Environment

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use the commands provided above to install the necessary dependencies.

3. **Database Setup**: The application uses SQLite for database management. The database will be created automatically when you run the application for the first time.

### Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server, and you can access the API at `http://127.0.0.1:8000`.

### API Endpoints

Here are the main API endpoints you can use:

- **Create a Student**: 
  - **Endpoint**: `POST /students/`
  - **Request Body**: 
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**: 
  - **Endpoint**: `GET /students/`
  
- **Create a Course**: 
  - **Endpoint**: `POST /courses/`
  - **Request Body**: 
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get Courses**: 
  - **Endpoint**: `GET /courses/`

- **Enroll a Student in a Course**: 
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Example**: To enroll student with ID 1 in course with ID 2, you would send a request to `POST /students/1/courses/2`.

### Example Usage

1. **Create a Student**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "Alice", "email": "alice@example.com"}'
   ```

2. **Create a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Physics", "level": "Intermediate"}'
   ```

3. **Enroll a Student in a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/1/courses/1"
   ```

## Documentation

For more detailed documentation, including examples and API references, please refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/).

## Conclusion

This system provides a robust framework for managing students and courses. We hope you find it useful for your educational management needs. If you have any questions or need further assistance, please feel free to reach out!
```