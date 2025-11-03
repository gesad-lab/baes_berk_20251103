Here's a detailed user manual for the Student Management application, structured in Markdown format:

```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and view students by their names.

## Main Functions

- **Add Student**: Users can input a student's name and add it to the database.
- **View Students**: Users can view a list of all students stored in the database.

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

- Ensure you have Python 3.11+ installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- Ensure that you have Tkinter installed for the GUI. Tkinter is usually included with Python installations. If you encounter issues, refer to the installation instructions for your operating system.

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd chatdev_app
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
pip install -r requirements.txt
```

### Step 4: Run the FastAPI Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### Step 5: Run the GUI Application

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, the student will be added to the database, and the list will refresh.

2. **Viewing Students**:
   - The list of students will automatically load when the application starts.
   - You can see all added students in the list box.

## Troubleshooting

- If you encounter a `ModuleNotFoundError: No module named 'tkinter'`, ensure that Tkinter is installed. You can install it using the following commands based on your operating system:
  - For Ubuntu/Debian:
    ```bash
    sudo apt-get install python3-tk
    ```
  - For Windows, Tkinter should be included with your Python installation. If not, consider reinstalling Python.

## Additional Notes

- The database schema is created automatically on startup, so there is no need for manual database setup.
- The application returns JSON responses for API requests, which can be tested using tools like Postman or directly through the GUI.

## Conclusion

This Student Management Application provides a simple interface for managing student records. With the FastAPI backend and Tkinter GUI, it serves as a great starting point for learning about web applications in Python.
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and troubleshooting tips, ensuring that users can effectively utilize the software.