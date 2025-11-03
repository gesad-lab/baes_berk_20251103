Here's a detailed user manual for the Student Management application, including installation instructions, main functions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing students and courses, allowing users to create and manage student records and course information.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create and manage courses with associated names and levels.
- **Database Management**: Migrate the database schema to include new entities while preserving existing data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-app.git
   cd student-management-app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   uvicorn
   ```

4. **Run Database Migrations**:
   To create the necessary database tables, run the following command:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   You can start the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

### Accessing the Application

Once the application is running, you can access it via your web browser at `http://127.0.0.1:8000`.

### API Endpoints

The application exposes several API endpoints for managing students and courses.

#### Student Endpoints

- **Create Student**:
  - **Endpoint**: `POST /students`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students`

- **Get Student by ID**:
  - **Endpoint**: `GET /students/{id}`

- **Update Student**:
  - **Endpoint**: `PUT /students/{id}`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Delete Student**:
  - **Endpoint**: `DELETE /students/{id}`

#### Course Endpoints

- **Create Course**:
  - **Endpoint**: `POST /courses`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses`

- **Get Course by ID**:
  - **Endpoint**: `GET /courses/{id}`

- **Update Course**:
  - **Endpoint**: `PUT /courses/{id}`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```

- **Delete Course**:
  - **Endpoint**: `DELETE /courses/{id}`

## Conclusion

This application provides a straightforward interface for managing students and courses. By following the installation and usage instructions, you can easily set up and interact with the application. For further details, please refer to the code documentation or reach out for support.
```

This manual provides a comprehensive overview of the Student Management application, ensuring that users can easily install and utilize its features.