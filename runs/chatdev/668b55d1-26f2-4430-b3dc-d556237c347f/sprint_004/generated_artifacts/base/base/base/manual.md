```markdown
# Student Management Application

A simple web application for managing student records using FastAPI and SQLite.

## Overview

The Student Management Application allows users to add and manage student records with a focus on simplicity and ease of use. The application features a graphical user interface (GUI) built with Tkinter, which communicates with a FastAPI backend to handle student data.

## Main Functions

- **Add Student**: Users can enter a student's name and submit it to the database.
- **Database Persistence**: Student records are stored in an SQLite database, which is created automatically on startup.
- **JSON Responses**: The API returns responses in JSON format, ensuring compatibility with various clients.

## Installation

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

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended) and install the required dependencies:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the FastAPI Backend

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 4: Run the GUI

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## Usage

1. **Open the GUI**: The Student Management application window will appear.
2. **Enter Student Name**: Type the name of the student you wish to add in the input field.
3. **Add Student**: Click the "Add Student" button to submit the name. A success message will appear if the student is added successfully.
4. **Error Handling**: If the server is not running or if the name field is empty, appropriate error messages will be displayed.

## API Endpoints

The application exposes the following API endpoint:

- **POST /students/**: Add a new student with a JSON body containing the `name` field.

### Example Request

```http
POST /students/
Content-Type: application/json

{
  "name": "John Doe"
}
```

### Example Response

```json
{
  "id": 1,
  "name": "John Doe"
}
```

## Conclusion

The Student Management Application provides a straightforward way to manage student records with a user-friendly interface. By following the installation and usage instructions, users can easily set up and run the application.

For any issues or feature requests, please contact the development team.
```