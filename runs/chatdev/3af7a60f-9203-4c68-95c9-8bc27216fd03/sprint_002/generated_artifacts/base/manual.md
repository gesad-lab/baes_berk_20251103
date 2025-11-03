Here's a detailed user manual for the Student Management web application, structured in Markdown format as requested:

```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite.

## Main Functions

The Student Management application allows users to:

- Add a new student with a name.
- Retrieve a list of all students.
- Interact with the application through a user-friendly GUI built with Tkinter.

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

2. **Open the GUI**:
   In another terminal, run the following command to start the Tkinter GUI:
   ```bash
   python gui.py
   ```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Submit" button.
   - A message will appear indicating whether the student was added successfully.

2. **Retrieving Students**:
   - The API endpoint to retrieve all students is available at `http://127.0.0.1:8000/students/`.
   - You can use tools like Postman or your browser to access this endpoint and view the list of students in JSON format.

## API Endpoints

- **POST /students/**: Add a new student.
  - Request Body: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - Response: 
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

- **GET /students/**: Retrieve a list of students.
  - Response: 
    ```json
    [
      {
        "id": 1,
        "name": "Student Name"
      },
      ...
    ]
    ```

## Additional Information

- The database schema is created automatically on startup, ensuring that the application is ready to use without any additional setup.
- The application uses SQLite for data persistence, making it lightweight and easy to manage.

## Support

For any issues or questions, please reach out to the development team at ChatDev.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and API details, ensuring that users can effectively interact with the software.