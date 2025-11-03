Here's the `manual.md` file for the software, detailing the main functions, installation of environment dependencies, and usage instructions:

```markdown
# Student Management System

A simple application for managing student records, including adding and retrieving student information.

## Main Functions

The Student Management System allows users to:

- **Add a Student**: Enter a student's name and email to create a new student record.
- **Retrieve Students**: View a list of all students along with their names and email addresses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the FastAPI Server**:
   Start the FastAPI server to handle API requests:
   ```bash
   uvicorn api:router --reload
   ```

2. **Launch the GUI**:
   Open a new terminal window (keeping the FastAPI server running) and execute:
   ```bash
   python main.py
   ```

3. **Interacting with the GUI**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to submit the information.
   - If successful, you will see a confirmation message displaying the added student's name and email.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file `students.db` will be created in the project directory upon running the application for the first time.
- **Data Preservation**: The application is designed to preserve existing student data during updates to the database schema.

## Troubleshooting

- If you encounter issues with Tkinter not being installed, please ensure you have it available in your Python environment. Tkinter is included with standard Python installations, but if you need to install it, you can do so using:
  ```bash
  sudo apt-get install python3-tk  # For Ubuntu
  ```

## Conclusion

This Student Management System provides a straightforward interface for managing student records. With the ability to add and view students, it serves as a foundational tool for educational institutions or personal projects.

For further assistance, please refer to the code comments or reach out to the development team.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring users can effectively utilize the Student Management System.