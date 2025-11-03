```markdown
# Student Management Web Application

This is a simple web application for managing student records, specifically focusing on the Student entity with a name field. The application is built using Python, FastAPI, and SQLite, providing a RESTful API for creating and retrieving student records.

## Main Functions

- **Add Student**: Allows users to add a new student by providing a name.
- **Get Students**: Retrieves a list of all students stored in the database.
- **User Interface**: A simple GUI built with Tkinter for user interaction.

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Run the FastAPI Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

This will run the application on `http://127.0.0.1:8000`.

### Step 5: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Open the GUI**: Launch the GUI application by running `gui.py`.
2. **Add a Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, the added student's details will be displayed in the output area.
3. **View Students**: You can view the list of students by calling the GET endpoint `/students/` using a tool like Postman or directly from the GUI if implemented.

## API Endpoints

- **POST /students/**: Create a new student.
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

## Conclusion

This application provides a simple yet effective way to manage student records. By following the installation and usage instructions, you can easily set up and interact with the application. For any issues or feature requests, please contact the development team.

```
