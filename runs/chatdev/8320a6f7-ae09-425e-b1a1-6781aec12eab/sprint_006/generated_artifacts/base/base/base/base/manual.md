```markdown
# Student Management Application

A simple application for managing student records, including adding students and viewing their details.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **Show Students**: Displays a list of all students currently stored in the database, including their ID, name, and email.

## Installation

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
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   requests
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Migration

Before running the application, ensure that the database schema is updated to include the new email field in the Student entity. Run the migration script:

```bash
python migration_script.py
```

This script will add the email column to the existing Student table without losing any existing data.

## How to Use the Application

1. **Run the FastAPI Backend**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Run the GUI**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```

3. **Interacting with the Application**:
   - **Add Student**: Enter the student's name and email in the provided fields and click the "Add Student" button. If successful, you will see a confirmation message.
   - **Show Students**: Click the "Show Students" button to retrieve and display a list of all students in the database.

## Conclusion

This Student Management Application provides a straightforward interface for managing student records, allowing for easy addition and retrieval of student information. For any issues or further assistance, please refer to the documentation or contact support.
```