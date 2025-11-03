```markdown
# Student Management Web Application

This is a simple web application for managing student records, built using Python, FastAPI, and SQLite. The application allows users to create and list students with a required name field.

## Main Functions

- **Create Student**: Allows users to add a new student by providing a name.
- **List Students**: Displays a list of all students currently stored in the database.

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

- Ensure you have Python 3.11+ installed on your machine.
- Install `pip` if it is not already installed.

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

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Run the FastAPI Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be running at `http://127.0.0.1:8000`.

### Step 5: Access the API Documentation

You can access the interactive API documentation provided by FastAPI at:

```
http://127.0.0.1:8000/docs
```

## How to Use the Application

### Using the GUI

1. **Launch the GUI**: Run the GUI application by executing the following command in your terminal:

   ```bash
   python gui.py
   ```

2. **Create a Student**:
   - Enter the student's name in the input field.
   - Click the "Create Student" button.
   - A success message will be displayed if the student is created successfully.

3. **List Students**:
   - Click the "List Students" button.
   - The list of students will be displayed in the list box below.

### Using the API Directly

You can also interact with the API directly using tools like Postman or curl.

- **Create a Student**:

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe"}'
```

- **List Students**:

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

## Conclusion

This application provides a simple interface for managing student records. You can extend its functionality by adding more fields or features as needed. For any issues or feature requests, please reach out to the development team.

Happy coding!
```