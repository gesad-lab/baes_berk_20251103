```markdown
# Student Management Application

A simple web application for managing student records using Python, FastAPI, and SQLite.

## Main Functions

The Student Management Application allows users to:

- **Add a Student**: Enter a student's name and add it to the database.
- **View Students**: Retrieve and display a list of all students stored in the database.

## Installation

To run the Student Management Application, you need to install the required dependencies. Follow the steps below to set up your environment:

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
   requests
   ```
   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the FastAPI Server**:
   Open a terminal and navigate to the `student_app` directory. Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   In another terminal, run the following command to start the graphical user interface:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - In the GUI window, enter the student's name in the input field.
   - Click the "Add Student" button. If successful, you will see a confirmation message in the output area.

2. **Viewing Students**:
   - Click the "View Students" button to retrieve and display all students in the database. The output area will show the list of students with their IDs and names.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
  - **Request Body**: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - **Response**: Returns the created student object.

- **GET /students/**: Retrieve all students.
  - **Response**: Returns a list of student objects.

## Notes

- Ensure that the FastAPI server is running before using the GUI to avoid connection errors.
- The database schema will be created automatically on startup, so there is no need for manual setup.

## Conclusion

This Student Management Application is a simple yet effective way to manage student records using modern web technologies. Feel free to explore and modify the code to fit your needs!
```