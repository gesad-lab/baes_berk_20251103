Here's a detailed user manual for the Student Management web application, structured in Markdown format:

```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and retrieve student information.

## Main Functions

- **Add Student**: Users can add a new student by providing their name.
- **Retrieve Student**: Users can retrieve a student's information by their unique ID.

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
pip install fastapi[all] sqlalchemy requests
```

### Step 4: Run the Application

Start the FastAPI application:

```bash
uvicorn main:app --reload
```

The application will be running at `http://127.0.0.1:8000`.

## Using the Application

### Web Interface

To interact with the application, you can use the provided GUI built with Tkinter or directly use API endpoints.

#### Using the GUI

1. Run the GUI application:

   ```bash
   python gui.py
   ```

2. The GUI window will open. Enter the student's name in the input field and click the "Add Student" button.
3. A message will appear indicating whether the student was added successfully or if there was an error.

#### Using API Endpoints

You can also interact with the application using HTTP requests. Below are the available endpoints:

- **Add Student**
  - **Endpoint**: `POST /students`
  - **Request Body**:
    ```json
    {
      "name": "Student Name"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

- **Retrieve Student**
  - **Endpoint**: `GET /students/{student_id}`
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

### Error Handling

If you try to retrieve a student that does not exist, you will receive a 404 error with the message:

```json
{
  "detail": "Student not found"
}
```

## Conclusion

This application provides a simple interface for managing student records. You can easily add and retrieve students using either the GUI or the API endpoints. For further enhancements, consider adding more features such as updating or deleting student records.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, installation instructions, and usage guidelines, ensuring users can effectively interact with the software.