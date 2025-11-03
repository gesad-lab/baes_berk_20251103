```markdown
# Student Management Web Application

A simple web application for managing student records using FastAPI and SQLite.

## Main Functions

The Student Management Web Application allows users to:

- Add a new student with a name.
- View a list of all students stored in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
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

## Running the Application

1. **Start the FastAPI server**:
   Open a terminal and navigate to the `student_app` directory. Run the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Run the GUI application**:
   Open another terminal (keeping the FastAPI server running) and run:
   ```bash
   python gui.py
   ```
   This will launch the Student Management GUI.

## How to Use the Application

### Adding a Student

1. In the GUI, enter the student's name in the input field.
2. Click the "Add Student" button.
3. If successful, you will see a confirmation message in the output area.

### Viewing Students

1. Click the "Show Students" button in the GUI.
2. The application will display a list of all students currently stored in the database.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Create a new student.
  - **Request Body**: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - **Response**: 
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

- **GET /students/**: Retrieve a list of all students.
  - **Response**: 
    ```json
    [
      {
        "id": 1,
        "name": "Student Name"
      },
      ...
    ]
    ```

## Conclusion

This Student Management Web Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application. For any issues or further assistance, feel free to reach out to the support team.
```