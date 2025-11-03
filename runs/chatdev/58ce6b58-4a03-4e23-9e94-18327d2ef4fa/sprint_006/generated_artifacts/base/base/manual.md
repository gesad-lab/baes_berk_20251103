# ChatDev Student-Course Management System

A comprehensive system for managing students and their associated courses. This software allows users to create and manage student records, as well as course offerings, with a seamless relationship between the two entities.

## Main Functions

- **Student Management**: Create, retrieve, and manage student records, including their associated courses.
- **Course Management**: Create and retrieve course offerings.
- **Relationship Management**: Associate students with multiple courses and manage these relationships effectively.

## Quick Install

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

## How to Use the Software

### Running the Application

1. **Start the FastAPI Server**:
   Run the following command to start the server:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

### API Endpoints

#### Student Management

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]  // Optional: List of course IDs to associate with the student
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: List of all students.

#### Course Management

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Retrieve All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: List of all courses.

### Database Migration

The application uses Alembic for database migrations. To apply migrations, ensure that the database is set up correctly and run:
```bash
alembic upgrade head
```

### Notes

- Ensure that the database file (`students.db`) is created in the project directory.
- The application uses SQLite for simplicity, but can be configured to use other databases by modifying the `DATABASE_URL` in `database.py`.

## Conclusion

This system provides a robust framework for managing students and courses, with a focus on maintaining relationships between entities. For further assistance, please refer to the code comments or reach out to the development team.