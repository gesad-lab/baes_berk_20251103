Here's a detailed user manual for the Student Management application, structured in Markdown format:

```markdown
# Student Management Application

A simple web application to manage student records using FastAPI and SQLite.

## Main Functions

- **Add Student**: Allows users to add a new student by entering their name.
- **Fetch Students**: Retrieves and displays a list of all students in the database.

## Quick Install

To run the Student Management application, you need to set up your environment and install the required dependencies.

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Install Dependencies**:
   You can install the required dependencies using pip. Run the following command in your terminal:
   ```bash
   pip install fastapi[all] sqlalchemy requests
   ```

3. **Run the FastAPI Application**:
   Navigate to the directory containing `main.py` and run the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

4. **Run the GUI**:
   In a separate terminal, navigate to the same directory and run:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Open the GUI**:
   After running `gui.py`, a window will appear.

2. **Add a Student**:
   - Enter the student's name in the input field labeled "Student Name".
   - Click the "Add Student" button. If successful, the student will be added to the database.

3. **Fetch Students**:
   - Click the "Fetch Students" button to retrieve and display the list of all students in the application. The names will appear in the list box below.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - **Request Body**: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - **Response**: Returns the created student object.

- **GET /students/**: Retrieve the list of all students.
  - **Response**: Returns a JSON array of student objects.

## Database

The application uses SQLite for data persistence. The database schema is automatically created on startup, ensuring that the necessary tables are available for storing student records.

## Troubleshooting

- If you encounter issues with the application not starting, ensure that all dependencies are installed correctly and that you are using Python 3.11 or higher.
- Check the terminal for any error messages that may indicate what went wrong.

## Conclusion

This Student Management application provides a simple interface for managing student records. With FastAPI and SQLite, it offers a lightweight solution for educational institutions or personal projects. For further enhancements, consider adding features like editing or deleting student records.
```

This manual provides a comprehensive guide for users to understand the application, install it, and utilize its features effectively.