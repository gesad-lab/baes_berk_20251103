```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and view students by their names.

## Main Functions

- **Add Student**: Users can enter a student's name and submit it to the backend, which will store the information in an SQLite database.
- **View Students**: Users can retrieve and display a list of all students stored in the database.

## Installation Instructions

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

The application will be running at `http://127.0.0.1:8000`.

### Step 5: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Add a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Submit" button. A confirmation message will appear if the student is added successfully.

2. **View Students**:
   - Click the "View Students" button in the GUI.
   - A list of all students will be displayed, showing their IDs and names.

## API Endpoints

The FastAPI application exposes the following endpoints:

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

- **GET /students/**: Retrieve a list of all students.
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

This Student Management Application provides a simple interface for managing student records. By following the installation instructions and using the GUI, users can easily add and view students. For any issues or further assistance, please refer to the documentation or contact support.
```