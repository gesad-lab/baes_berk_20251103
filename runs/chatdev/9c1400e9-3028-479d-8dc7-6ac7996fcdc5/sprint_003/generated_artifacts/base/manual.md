```markdown
# Student Registration System

A simple application for registering students with their names and email addresses.

## Main Functions

The Student Registration System allows users to:

- Register new students by providing their name and email address.
- Store student information in a database.
- Retrieve and display confirmation of student registration.

## Quick Install

To set up the environment and run the application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/student-registration.git
   cd student-registration
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi[all] sqlalchemy alembic requests
   ```

4. **Run the database migration to add the email field:**
   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000/docs
   ```
   This will display the interactive API documentation.

## How to Use the Application

### Registering a Student

1. **Open the GUI:**
   Run the `gui.py` script to launch the student registration interface.
   ```bash
   python gui.py
   ```

2. **Fill in the Student Information:**
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.

3. **Submit the Form:**
   Click the "Submit" button to register the student. If successful, a confirmation message will be displayed.

### API Endpoints

- **POST /students**
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response:**
    - Status Code: 201 Created
    - Body:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

## Database Migration

The application uses Alembic for database migrations. The migration script `migration_script.py` adds an email field to the existing Student entity while preserving existing data. 

### Migration Steps

1. **Add the email column as nullable.**
2. **Update existing records to have a default value (empty string).**
3. **Alter the column to be non-nullable.**

## Additional Resources

For more information on FastAPI, SQLAlchemy, and Alembic, please refer to the following documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

Feel free to reach out for support or contributions to enhance the Student Registration System!
```