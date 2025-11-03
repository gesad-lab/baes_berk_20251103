```markdown
# Student Management Web Application

This application allows users to manage student records through a simple web interface. It is built using Python, FastAPI, and SQLite, providing a RESTful API for creating and retrieving student information.

## Main Functions

- **Create a Student**: Users can submit a student's name, which will be stored in the SQLite database.
- **Retrieve a Student**: Users can retrieve a student's details by their unique ID.

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

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended) and install the required dependencies:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the FastAPI Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be running at `http://127.0.0.1:8000`.

### Step 4: Access the API Documentation

FastAPI provides an interactive API documentation interface. You can access it at:

```
http://127.0.0.1:8000/docs
```

## How to Use the Application

### Using the API

1. **Create a Student**:
   - Endpoint: `POST /students/`
   - Request Body:
     ```json
     {
       "name": "John Doe"
     }
     ```
   - Response:
     ```json
     {
       "id": 1,
       "name": "John Doe"
     }
     ```

2. **Retrieve a Student**:
   - Endpoint: `GET /students/{student_id}`
   - Example: `GET /students/1`
   - Response:
     ```json
     {
       "id": 1,
       "name": "John Doe"
     }
     ```

### Using the GUI

The application also includes a simple GUI built with Tkinter for easier interaction:

1. Run the GUI application:
   ```bash
   python main.py
   ```

2. Enter the student's name in the input field and click "Submit". The application will send a request to the FastAPI backend to create a new student record.

3. The response will be displayed in the GUI, indicating whether the student was created successfully or if there was an error.

## Conclusion

This Student Management Web Application provides a straightforward way to manage student records using modern web technologies. The combination of FastAPI for the backend and Tkinter for the GUI makes it easy to interact with the application.

For further customization or enhancements, feel free to modify the code as per your requirements.
```