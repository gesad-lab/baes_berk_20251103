```markdown
# Student Management System

A simple application for managing student records, including adding students with their names and email addresses.

## Main Functions

- **Add Student**: Allows users to add a new student by providing their name and email address.
- **Email Validation**: Ensures that the email address provided is in a valid format.
- **Data Persistence**: Stores student records in a SQLite database, preserving existing data during schema updates.

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
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the FastAPI Application**:
   Start the FastAPI server by running the following command in your terminal:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the GUI**:
   Open the `gui.py` file and run it:
   ```bash
   python gui.py
   ```
   This will open a simple Tkinter GUI for adding students.

3. **Add a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to submit the information.
   - A message will appear indicating whether the student was added successfully or if there was an error.

## Database Migration

The application includes a migration script (`migration.py`) that adds the email field to the existing Student table without losing any existing data. To run the migration, execute the following command:
```bash
python migration.py
```

## Additional Information

- **API Documentation**: You can access the automatically generated API documentation at `http://127.0.0.1:8000/docs`.
- **Database**: The application uses SQLite for data storage, and the database file is located in the project directory as `students.db`.

## Conclusion

This Student Management System provides a straightforward way to manage student records with essential features. Feel free to extend its functionality or integrate it with other systems as needed.
```