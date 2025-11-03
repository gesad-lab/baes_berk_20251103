```markdown
# Student Management Web Application

This manual provides a comprehensive guide to using the Student Management Web Application built with Python, FastAPI, and SQLite. The application allows users to manage student records by adding and viewing students.

## Main Functions

- **Add Student**: Users can enter a student's name and add it to the database.
- **View Students**: Users can retrieve and view a list of all students stored in the database.

## Installation Instructions

To run the Student Management Web Application, you need to set up the environment and install the required dependencies. Follow the steps below:

### Step 1: Install Python

Ensure you have Python 3.11+ installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 3: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 4: Install Dependencies

Install the required dependencies using pip. Make sure you have `requirements.txt` in the project directory:

```bash
pip install -r requirements.txt
```

### Step 5: Run the FastAPI Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### Step 6: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, the added student will be displayed in the output area.

2. **Viewing Students**:
   - Click the "View Students" button in the GUI.
   - The application will retrieve and display a list of all students from the database.

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

This Student Management Web Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and interact with the application. For any issues or feature requests, please contact the development team.
```