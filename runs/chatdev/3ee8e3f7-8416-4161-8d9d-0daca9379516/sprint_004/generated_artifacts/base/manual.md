Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management Application

A FastAPI-based application for managing students and courses, allowing users to create and retrieve student and course records.

## Main Functions

- **Create Student**: Add a new student to the database with a name and email.
- **Retrieve Students**: Get a list of all students in the database.
- **Create Course**: Add a new course to the database with a name and level.
- **Retrieve Courses**: Get a list of all courses in the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, ensure that the database schema is up to date. The migration script will create the necessary tables and preserve existing student data.

1. **Run the migration script**:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by FastAPI.

3. **Create a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

4. **Retrieve Students**:
   - **Endpoint**: `GET /students/`
   - **Response**: A list of all students in the database.

5. **Create a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```

6. **Retrieve Courses**:
   - **Endpoint**: `GET /courses/`
   - **Response**: A list of all courses in the database.

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database file is located at `./students.db`.
- **CORS**: Cross-Origin Resource Sharing (CORS) is enabled for all origins, which allows the application to be accessed from different domains.

## Troubleshooting

If you encounter any issues, ensure that all dependencies are installed correctly and that the database migrations have been applied. Check the server logs for any error messages.

For further assistance, please contact the support team or refer to the FastAPI documentation for more information on API development and usage.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and troubleshooting tips. Let me know if you need any modifications or additional sections!