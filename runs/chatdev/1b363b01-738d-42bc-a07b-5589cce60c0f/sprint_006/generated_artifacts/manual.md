```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can create, read, and manage relationships between these entities seamlessly.

## Main Functions

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records, including the ability to assign teachers to courses.
- **Teacher Management**: Create and retrieve teacher records.
- **Relationships**: Establish relationships between students and courses, as well as between courses and teachers.

## Quick Install

To get started, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy alembic uvicorn
```

Make sure you have Python 3.7 or higher installed on your machine.

## Setting Up the Environment

1. **Clone the Repository**: Clone the repository containing the code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Run the following command to install all necessary dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**: The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## Running the Application

To run the application, execute the following command:

```bash
python main.py
```

The application will start on `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Students

- **Create a Student**: `POST /students`
  - Request Body: 
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get Students**: `GET /students`

### Courses

- **Create a Course**: `POST /courses`
  - Request Body: 
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner",
      "teacher_id": 1  // Optional, specify if assigning a teacher
    }
    ```

- **Get Courses**: `GET /courses`

### Teachers

- **Create a Teacher**: `POST /teachers`
  - Request Body: 
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Get Teachers**: `GET /teachers`

## Database Migration

The application uses Alembic for database migrations. The migration scripts are included in the `migrations` folder. The database schema is updated automatically when the application starts, preserving existing data.

## Conclusion

This Course Management System is designed to simplify the management of educational entities. With its intuitive API and easy setup, you can quickly get started managing students, courses, and teachers.

For further assistance, please refer to the API documentation or reach out to our support team.
```