Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management API

A simple API for managing students and courses.

## Introduction

This API allows users to create and manage students and courses. The main functions include:

- Creating and retrieving student records.
- Creating and retrieving course records.
- The API is built using FastAPI and SQLAlchemy, providing a robust and efficient way to handle data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

4. **Run the database migration to create the necessary tables:**
   ```bash
   python main.py
   ```

## How to Use the API

### Starting the Server

To start the FastAPI server, run the following command:

```bash
uvicorn routers:router --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### Student Endpoints

- **Create a Student**
  - **Endpoint:** `POST /students/`
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get a Student by ID**
  - **Endpoint:** `GET /students/{student_id}`
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

#### Course Endpoints

- **Create a Course**
  - **Endpoint:** `POST /courses/`
  - **Request Body:**
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get a Course by ID**
  - **Endpoint:** `GET /courses/{course_id}`
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

## Database Schema

The API uses SQLite as the database. The following tables are created:

- **students**
  - `id`: Integer, primary key
  - `name`: String, required
  - `email`: String, required

- **courses**
  - `id`: Integer, primary key
  - `name`: String, required
  - `level`: String, required

### Database Migration

The database migration is handled in `main.py`, which creates the necessary tables without affecting existing student data.

## Conclusion

This API provides a straightforward way to manage students and courses. For further customization or additional features, feel free to modify the code as needed.

For more detailed documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```

This manual provides a comprehensive overview of the API, installation instructions, usage examples, and details about the database schema. Let me know if you need any further modifications or additional sections!