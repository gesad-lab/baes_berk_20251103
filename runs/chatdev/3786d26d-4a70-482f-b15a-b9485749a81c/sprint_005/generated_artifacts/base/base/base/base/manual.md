Here's the `manual.md` file for the Student Management web application:

```markdown
# Student Management Web Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite.

## Main Functions

- **Add Student**: Allows users to add a new student by providing their name.
- **Get Students**: Fetches and displays a list of all students stored in the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.11+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Application

1. **Start the FastAPI Server**:
   In your terminal, navigate to the directory containing `main.py` and run:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Run the GUI Application**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```
   This will open a Tkinter window where you can interact with the API.

## How to Use the Application

### Adding a Student

1. In the GUI window, enter the student's name in the "Student Name" field.
2. Click the "Add Student" button.
3. A message will appear indicating whether the student was added successfully or if there was an error.

### Getting Students

1. Click the "Get Students" button in the GUI.
2. The application will fetch and display a list of all students currently stored in the database.

## Troubleshooting

- **Server Not Starting**: Ensure that you have installed all dependencies correctly and that no other application is using port 8000.
- **Database Issues**: If you encounter issues with the SQLite database, ensure that the `students.db` file is not locked by another process.

## Conclusion

This Student Management web application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and interact with the application. For further enhancements or features, feel free to explore the FastAPI documentation and expand the application as needed.
```

This manual provides a comprehensive guide for users to understand the application, install dependencies, and utilize its features effectively.