# README.md

# Project Title

## Introduction

This project is a FastAPI application designed for managing courses in an educational platform. 

## Setup Instructions

To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare the database**:
   - Make sure you have SQLite installed on your machine.
   - Update your `.env` file with the required SQLite connection strings. You can create a `.env` file in the project root if it does not exist.

   Example `.env` file content:
   ```env
   DATABASE_URL=sqlite:///./test.db
   ```

5. **Run migrations** (if applicable):
    ```bash
    alembic upgrade head
    ```

## API Usage Instructions

### Base URL

The base URL for all API endpoints is `http://localhost:8000`.

### Endpoints

#### Create Course

- **Endpoint**: `/courses/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "title": "Course Title",
        "description": "Course Description",
        "instructor": "Instructor Name"
    }
    ```
- **Response**: Returns the created course object including the assigned ID.

#### Get All Courses

- **Endpoint**: `/courses/`
- **Method**: `GET`
- **Response**: Returns a list of all courses.

#### Get Course by ID

- **Endpoint**: `/courses/{id}`
- **Method**: `GET`
- **Response**: Returns the course with the specified ID.

#### Update Course

- **Endpoint**: `/courses/{id}`
- **Method**: `PUT`
- **Request Body**:
    ```json
    {
        "title": "Updated Course Title",
        "description": "Updated Course Description",
        "instructor": "Updated Instructor Name"
    }
    ```
- **Response**: Returns the updated course object.

#### Delete Course

- **Endpoint**: `/courses/{id}`
- **Method**: `DELETE`
- **Response**: Returns a success message.

## Testing

To run the tests, ensure you have installed `pytest` and the necessary testing libraries. Then, run the following command:

```bash
pytest
```

This will execute the test suite defined in the `tests/` directory.

## Conclusion

This README provides the essential setup and usage instructions for the API. For additional information or troubleshooting, refer to the project's documentation or contact the development team.