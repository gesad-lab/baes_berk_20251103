```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and list students by their names.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **List Students**: Users can view a list of all students stored in the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository** (if applicable):
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
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Application

1. **Start the FastAPI Server**:
   Open a terminal and navigate to the `student_app` directory. Run the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI**:
   In another terminal, run the GUI application:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button. A success message will appear if the student is added successfully.

2. **Listing Students**:
   - Click the "List Students" button in the GUI.
   - A window will pop up displaying the list of students with their IDs and names.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Adds a new student.
  - **Request Body**: JSON object with the student's name.
  - **Response**: JSON object with the created student's ID and name.

- **GET /students/**: Retrieves a list of students.
  - **Query Parameters**: 
    - `skip`: Number of records to skip (default is 0).
    - `limit`: Maximum number of records to return (default is 10).
  - **Response**: JSON array of student objects.

## Additional Notes

- The database schema is automatically created on startup, so there is no need for manual migrations.
- Ensure that the FastAPI server is running before using the GUI to avoid connection errors.

For further assistance, please refer to the FastAPI documentation or contact support.
```