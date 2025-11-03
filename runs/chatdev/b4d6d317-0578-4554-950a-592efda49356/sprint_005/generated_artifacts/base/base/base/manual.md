Here's the `manual.md` file that outlines the user manual for the Student Management application, including installation instructions, main functions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including adding and viewing students with their names and email addresses.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address, which will be stored in the database.
- **Show Students**: Displays a list of all students currently stored in the database, showing their IDs, names, and email addresses.

## Quick Install

To run the Student Management application, you need to set up your environment and install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student_management_app.git
   cd student_management_app
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have `pip` installed, then run:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## How to Use the Application

1. **Adding a Student**:
   - Open the application interface.
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button.
   - If successful, a confirmation message will appear in the output area.

2. **Viewing Students**:
   - Click the "Show Students" button.
   - The application will display a list of all students, including their IDs, names, and email addresses.

## Additional Information

- Ensure that your Python environment is set up correctly and that all dependencies are installed.
- The application uses SQLite for the database, which is lightweight and requires no additional setup.
- If you encounter any issues, please check the console for error messages or refer to the FastAPI documentation for troubleshooting.

## Conclusion

The Student Management Application is a straightforward tool for managing student records. With its simple interface and robust backend, it provides an efficient way to add and view student information.

For further assistance, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/) or reach out to the development team.
```

This manual provides a comprehensive overview of the application, including installation steps, main functionalities, and usage instructions, ensuring that users can effectively utilize the software.