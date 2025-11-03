```markdown
# Student Management Web Application

This document serves as a user manual for the Student Management Web Application built using Python, FastAPI, and SQLite. The application allows users to manage student records by adding and viewing students.

## Main Functions of the Software

- **Add Student**: Users can input a student's name and add it to the database.
- **Show Students**: Users can view a list of all students stored in the database.

## Installation of Environment Dependencies

To run the Student Management Web Application, you need to install the required dependencies. Follow these steps:

1. **Ensure Python 3.11+ is installed**: You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the repository**: If you haven't already, clone the repository containing the application code.

   ```bash
   git clone <repository-url>
   cd student_app
   ```

3. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the required dependencies**: Create a `requirements.txt` file with the following content:

   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   ```

   Then, run the following command to install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Start the FastAPI server**: Open a terminal and navigate to the directory containing `main.py`. Run the following command to start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Run the GUI**: Open another terminal (or command prompt) and navigate to the same directory. Run the following command to start the GUI:

   ```bash
   python gui.py
   ```

3. **Using the GUI**:
   - **Add Student**: Enter the student's name in the input field and click the "Add Student" button. If successful, the student will be added to the database, and you will see a confirmation message.
   - **Show Students**: Click the "Show Students" button to retrieve and display a list of all students currently stored in the database.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Adds a new student. Requires a JSON body with the `name` field.
  
  Example request:
  ```json
  {
      "name": "John Doe"
  }
  ```

- **GET /students/**: Retrieves a list of students. Supports pagination with `skip` and `limit` query parameters.

## Conclusion

This Student Management Web Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application. For any issues or further assistance, please refer to the documentation or contact support.
```