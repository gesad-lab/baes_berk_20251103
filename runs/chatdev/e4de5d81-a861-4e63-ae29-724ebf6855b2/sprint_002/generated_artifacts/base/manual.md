```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to create and retrieve student records with a focus on ease of use and best practices in software development.

## Main Functions

- **Create Student**: Allows users to add a new student by providing a name.
- **Get Students**: Retrieves a list of all students stored in the database.

## Installation Guide

To set up the environment and run the application, follow these steps:

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

The application will be accessible at `http://127.0.0.1:8000`.

### Step 5: Access the API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

## How to Use the Application

### Using the API

You can interact with the API using tools like Postman, cURL, or directly through the Swagger UI.

#### Create a Student

To create a new student, send a POST request to `/students/` with a JSON body:

```json
{
  "name": "John Doe"
}
```

#### Get Students

To retrieve the list of students, send a GET request to `/students/`. You can also use query parameters `skip` and `limit` to paginate results:

```
GET /students/?skip=0&limit=10
```

### Using the GUI

The application also includes a simple GUI built with Tkinter for easier interaction.

1. Run the GUI by executing the `gui.py` script:

   ```bash
   python gui.py
   ```

2. The GUI will open, allowing you to:
   - Enter a student's name and click "Add Student" to create a new student record.
   - Click "Get Students" to retrieve and display the list of students.

## Conclusion

This Student Management Web Application provides a straightforward way to manage student records using modern web technologies. Feel free to customize and extend the application as needed!

For any questions or support, please contact the development team.
```