Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management System

A simple and efficient application for managing students and courses.

## Main Functions

The Student Management System provides the following functionalities:

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records.
- **Database Management**: Automatically handles database creation and migration to preserve existing data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student_management_system.git
   cd student_management_system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Install Tkinter** (if not already installed):
   Tkinter is included with Python installations on most systems. If you encounter issues, please refer to your system's documentation for installation instructions.

## How to Use

### Running the Application

1. **Start the Database**:
   The application will automatically create the database and tables when you run the main application file. 

2. **Run the Application**:
   Execute the following command to start the application:
   ```bash
   python main.py
   ```

3. **Access the GUI**:
   The application will open a Tkinter window for managing students and courses.

### Using the API

You can also interact with the application through its API endpoints. Here are some examples:

- **Create a Student**:
   ```http
   POST /students/
   Content-Type: application/json

   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

- **Retrieve Students**:
   ```http
   GET /students/
   ```

- **Create a Course**:
   ```http
   POST /courses/
   Content-Type: application/json

   {
       "name": "Mathematics",
       "level": "Beginner"
   }
   ```

- **Retrieve Courses**:
   ```http
   GET /courses/
   ```

### Database Migration

The application uses Alembic for database migrations. When you run the application, it will check for existing tables and apply any necessary migrations to ensure that existing student data is preserved while adding new course tables.

## Conclusion

This Student Management System is designed to simplify the management of student and course records. With a user-friendly GUI and a robust API, it provides a comprehensive solution for educational institutions.

For further assistance or to report issues, please contact our support team.
```

This manual provides a clear overview of the software's capabilities, installation steps, and usage instructions, ensuring that users can effectively utilize the Student Management System.