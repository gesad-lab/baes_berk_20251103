Here is the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and SQLite.

## Main Functions

The Teacher Management System allows users to:

- **Create Students**: Register new students with their names, emails, and associated courses.
- **Create Courses**: Add new courses with specified names and levels.
- **Create Teachers**: Register new teachers with their names and emails.
- **View Students**: Retrieve a list of registered students.
- **View Courses**: Retrieve a list of available courses.
- **View Teachers**: Retrieve a list of registered teachers.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run the database migrations**:
   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Access the GUI**:
   - Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.
   - Alternatively, run the `gui.py` file to launch the graphical user interface:
     ```bash
     python gui.py
     ```

2. **Registering Students**:
   - Enter the student's name, email, and course IDs (comma-separated) in the respective fields and click "Create Student".

3. **Registering Courses**:
   - Enter the course name and level in the respective fields and click "Create Course".

4. **Registering Teachers**:
   - Enter the teacher's name and email in the respective fields and click "Create Teacher".

5. **Viewing Records**:
   - You can view the list of students, courses, and teachers by using the respective GET endpoints available in the API documentation.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is created in the project directory.
- **Migrations**: The application uses Alembic for database migrations. Ensure to run migrations whenever you make changes to the database schema.
- **API Documentation**: For more detailed API usage, refer to the automatically generated documentation at `http://127.0.0.1:8000/docs`.

## Support

For any issues or feature requests, please open an issue in the repository or contact support at support@yourcompany.com.

```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring that users can effectively utilize the Teacher Management System.