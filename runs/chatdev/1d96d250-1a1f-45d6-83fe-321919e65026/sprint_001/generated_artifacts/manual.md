Here's a detailed user manual for the Student Management application, structured in Markdown format as requested:

```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite.

## Main Functions

The Student Management application allows users to:

- Add new students by entering their names.
- Store student records in a SQLite database.
- Retrieve student records through a RESTful API.

## Installation

To run the Student Management application, you'll need to set up your environment and install the necessary dependencies. Follow these steps:

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

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install fastapi[all] sqlalchemy requests
```

### Step 4: Run the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## How to Use the Application

### Accessing the GUI

1. Run the `gui.py` script to launch the graphical user interface:

```bash
python gui.py
```

2. The GUI will prompt you to enter a student's name.

### Adding a Student

1. Enter the student's name in the provided text field.
2. Click the "Add Student" button.
3. If the student is added successfully, a success message will appear. If there is an error, an error message will be displayed.

### API Endpoints

The application exposes a RESTful API for managing students. Below are the available endpoints:

- **POST /students/**: Add a new student.
  - Request Body: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - Response: 
    - Status Code: 201 Created
    - Body:
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

## Database

The application uses SQLite for persistence. The database schema is created automatically on startup. The database file will be located in the same directory as the application code (`students.db`).

## Conclusion

This Student Management application provides a simple interface for managing student records. Feel free to modify and extend the application as needed to fit your requirements.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and API details, ensuring that users can easily understand and interact with the software.