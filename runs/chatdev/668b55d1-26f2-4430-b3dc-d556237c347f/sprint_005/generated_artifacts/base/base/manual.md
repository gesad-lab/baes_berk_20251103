Here's the user manual for the software, detailing the main functions, installation instructions, and usage guidelines.

```markdown
# Course Management Application

Manage courses and students effectively with our Course Management Application.

## Main Functions

The Course Management Application allows users to perform the following functions:

- **Create Students**: Add new students to the database with their name and email.
- **Create Courses**: Add new courses with a name and level.
- **Database Management**: The application manages a SQLite database to store student and course information.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-app.git
   cd course-management-app
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
   pydantic
   alembic
   uvicorn
   ```

## Usage

### Running the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

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
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```

### Database Migration

To ensure that the database schema is up to date with the latest changes, run the migration script:

```bash
alembic upgrade head
```

This will add the necessary columns and tables to the database while preserving existing student data.

## Conclusion

The Course Management Application is designed to simplify the management of students and courses. By following the installation and usage instructions, you can quickly set up and start using the application. For further assistance, please refer to the documentation or contact support.
```

This manual provides a comprehensive overview of the application, including installation steps, main functionalities, and how to interact with the API. Let me know if you need any modifications or additional information!