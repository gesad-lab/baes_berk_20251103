```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, retrieve, and associate these entities seamlessly.

## Main Functions

- **Student Management**: Create and manage student profiles, including their associated courses.
- **Course Management**: Create and manage courses, including assigning teachers to courses.
- **Teacher Management**: Create and manage teacher profiles.

## Quick Install

To get started, you need to install the required dependencies. You can do this using `pip` or `conda`.

### Using pip

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### Using conda

```bash
conda install fastapi -c conda-forge
conda install uvicorn -c conda-forge
conda install sqlalchemy -c conda-forge
conda install pydantic -c conda-forge
```

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd student_app
```

### 2. Run the Application

To run the application, execute the following command:

```bash
python main.py
```

This will start the FastAPI application on `http://127.0.0.1:8000`.

### 3. Access the API Documentation

Once the server is running, you can access the interactive API documentation at:

```
http://127.0.0.1:8000/docs
```

This documentation provides a user-friendly interface to interact with the API endpoints.

## API Endpoints

### Students

- **Create Student**: `POST /students/`
  - Request Body: 
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "courses": [1, 2]  // Optional list of course IDs
    }
    ```

- **Get Students**: `GET /students/`
  - Query Parameters: `skip`, `limit`

### Courses

- **Create Course**: `POST /courses/`
  - Request Body: 
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner",
      "teacher_id": 1  // Optional teacher ID
    }
    ```

- **Get Courses**: `GET /courses/`
  - Query Parameters: `skip`, `limit`

### Teachers

- **Create Teacher**: `POST /teachers/`
  - Request Body: 
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

## Database Migration

The application includes a migration script that ensures existing data is preserved while adding new relationships. The `migrate_database` function in `database.py` handles this process automatically when the application starts.

## Conclusion

The ChatDev Course Management System is designed to simplify the management of educational entities. With its intuitive API and robust functionality, you can easily manage students, courses, and teachers. For further assistance, feel free to reach out to our support team.

Happy coding!
```