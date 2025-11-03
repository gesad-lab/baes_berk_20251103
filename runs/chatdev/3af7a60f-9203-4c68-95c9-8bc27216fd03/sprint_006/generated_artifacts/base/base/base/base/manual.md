```markdown
# Student Management Application

A simple application for managing student records, including the ability to add students with their names and email addresses.

## Main Functions

- **Add Student**: Users can add a new student by entering their name and email address.
- **View Students**: Users can retrieve a list of all students stored in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migration**:
   Ensure that the database schema is updated to include the new email field. Run the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Open the GUI**:
   After starting the application, a GUI window will appear.

2. **Add a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Submit" button to add the student.

3. **View Results**:
   - After submission, a message will appear indicating whether the student was added successfully or if there was an error.

## Database Migration

The application uses Alembic for managing database migrations. The migration script `migration.py` includes the following steps:

- **Upgrade**: Adds the email column to the students table, updates existing records with a default email, and alters the column to be non-nullable.
- **Downgrade**: Removes the email column from the students table if needed.

## Additional Information

- **API Documentation**: The application exposes a RESTful API for managing students. You can access the API documentation at `http://127.0.0.1:8000/docs` after starting the application.
- **Error Handling**: The application includes basic error handling for invalid input.

For further assistance or feature requests, please contact the development team.

```
