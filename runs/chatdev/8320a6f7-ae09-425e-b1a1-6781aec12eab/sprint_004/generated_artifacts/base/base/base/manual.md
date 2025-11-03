```markdown
# Student Management Web Application

This is a simple web application designed to manage student records. It allows users to add and view students through a user-friendly interface. The application is built using Python, FastAPI, and SQLite.

## Main Functions

- **Add Student**: Users can enter a student's name and add it to the database.
- **Show Students**: Users can view the list of all students stored in the database.

## Installation Guide

To run the Student Management Web Application, you need to set up your environment and install the required dependencies. Follow the steps below:

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
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

The application will be running at `http://127.0.0.1:8000`.

### Step 5: Run the GUI Application

In a new terminal window, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Open the GUI application.
   - Enter the student's name in the provided text box.
   - Click the "Add Student" button.
   - If successful, a confirmation message will appear.

2. **Show Students**:
   - Click the "Show Students" button.
   - The list of students will be displayed in the output area.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Adds a new student.
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

- **GET /students/**: Retrieves a list of all students.
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

This Student Management Web Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and interact with the application. For any issues or feature requests, please reach out to the development team.

Happy coding!
```