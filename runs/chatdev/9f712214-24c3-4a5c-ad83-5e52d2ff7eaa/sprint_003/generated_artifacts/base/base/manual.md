Here's a detailed user manual for the Student Management application, structured in Markdown format as requested:

```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite.

## Main Functions

The Student Management Application allows users to:
- Create new student records with a name.
- Retrieve a list of existing students.

## Quick Install

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
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

## Running the Application

1. **Start the FastAPI server**:
   Navigate to the directory where `main.py` is located and run:
   ```bash
   uvicorn main:app --reload
   ```

   This will start the FastAPI server on `http://127.0.0.1:8000`.

2. **Open the GUI**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```

   This will open a Tkinter window where you can interact with the application.

## How to Use the Application

### Creating a Student

1. In the GUI window, enter the student's name in the input field.
2. Click the "Submit" button.
3. If successful, the application will display the created student record below the input field.

### Retrieving Students

- The application currently does not have a direct GUI feature to list students. However, you can access the API endpoint to retrieve students using a tool like Postman or curl:
  ```bash
  curl -X GET "http://127.0.0.1:8000/students/"
  ```

## API Documentation

### Create Student

- **Endpoint**: `POST /students/`
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

### Get Students

- **Endpoint**: `GET /students/`
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

## Troubleshooting

- If you encounter issues with Tkinter, ensure it is installed. You can install it via your package manager or ensure it is included in your Python installation.
- If the FastAPI server does not start, check for any errors in the terminal and ensure all dependencies are installed correctly.

## Conclusion

This application provides a straightforward interface for managing student records. For further enhancements, consider adding features like editing and deleting students, or implementing user authentication.

For any questions or support, please contact the development team.
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and API documentation, ensuring that users can effectively interact with the Student Management application.