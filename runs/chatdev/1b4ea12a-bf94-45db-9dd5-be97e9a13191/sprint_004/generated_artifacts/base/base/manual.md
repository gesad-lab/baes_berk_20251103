Here's a detailed user manual for the software, including the main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including adding, updating, and retrieving student information.

## Main Functions

- **Add Student**: Allows users to add a new student with a name and email address.
- **Update Student**: Enables users to update existing student information.
- **Retrieve Student**: Users can retrieve student details by their ID.
- **Database Management**: The application manages student data using a SQLite database.

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

   Ensure that you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   uvicorn
   ```

## Database Setup

Before running the application, you need to set up the database:

1. **Create the Database**:
   Run the following command to create the database and tables:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

2. **Run Migrations**:
   To apply the latest database schema changes, run:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Run the Application**:
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the Dashboard**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Add a New Student**:
   Use the `/students` endpoint to add a new student. You will need to provide the following JSON payload:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **Retrieve Student Information**:
   To retrieve a student's information, use the `/students/{id}` endpoint, replacing `{id}` with the student's ID.

5. **Update Student Information**:
   Use the `/students/{id}` endpoint with a PUT request to update a student's details.

## Additional Information

- **Database**: The application uses SQLite for data storage, and the database file is located in the project directory as `students.db`.
- **Schema Changes**: The recent update includes an email field in the Student entity, which is required for each student record.

For more detailed documentation and examples, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

```

This manual provides a comprehensive overview of the Student Management Application, guiding users through installation, setup, and usage. Let me know if you need any further modifications or additional sections!