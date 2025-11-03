# Student Application User Manual

## Overview

The Student Application is a simple web application built using Python, FastAPI, and SQLite. It allows users to manage student records by adding student names to a database. The application features a graphical user interface (GUI) for easy interaction.

## Main Functions

- **Add Student**: Users can enter a student's name and submit it to be stored in the SQLite database.
- **Database Persistence**: The application automatically creates the necessary database schema on startup, ensuring that all student records are saved persistently.

## Installation Instructions

To set up the environment and run the Student Application, follow these steps:

### Prerequisites

Ensure you have Python 3.11+ installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment (Optional)

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip. Create a `requirements.txt` file with the following content:

```
fastapi
uvicorn
sqlalchemy
pydantic
requests
```

Then run the following command:

```bash
pip install -r requirements.txt
```

### Step 4: Run the FastAPI Application

To start the FastAPI application, run the following command in the terminal:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 5: Run the GUI Application

In a new terminal window (keeping the FastAPI server running), run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Open the GUI**: After running `gui.py`, a window will appear prompting you to enter a student's name.
2. **Add a Student**: Type the student's name in the input field and click the "Add Student" button.
3. **View Results**: The application will display a message indicating whether the student was added successfully or if there was an error.

## API Endpoints

The application exposes the following API endpoint:

- **POST /students/**: Adds a new student with the provided name in JSON format.

### Example Request

```json
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

The Student Application provides a simple yet effective way to manage student records using modern web technologies. By following the installation and usage instructions, users can easily set up and interact with the application. For any further questions or support, please reach out to the development team.