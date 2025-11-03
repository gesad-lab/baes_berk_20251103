```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to create and retrieve student records through a user-friendly interface.

## Main Functions

- **Create Student**: Allows users to add a new student by entering their name.
- **Get Students**: Fetches and displays a list of all registered students.

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

It's a good practice to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install fastapi[all] sqlalchemy pydantic requests
```

### Step 4: Run the Application

Start the FastAPI application by running the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## How to Use the Application

### Using the API

You can interact with the API directly using tools like Postman or curl, or you can use the provided GUI.

#### Create a Student

To create a new student, send a POST request to the `/students/` endpoint with a JSON body containing the student's name:

```json
{
  "name": "John Doe"
}
```

#### Get Students

To retrieve the list of all students, send a GET request to the `/students/` endpoint.

### Using the GUI

The application also includes a simple GUI built with Tkinter for easier interaction.

1. Run the GUI script:

   ```bash
   python gui.py
   ```

2. The GUI will open, allowing you to:
   - Enter a student's name and click "Create Student" to add them.
   - Click "Get Students" to fetch and display the list of students.

## Conclusion

This application provides a straightforward way to manage student records using a modern web framework and a lightweight database. Feel free to explore and modify the code to suit your needs!

For any issues or feature requests, please contact the development team.
```