Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management System

A simple application for managing student records, including adding and retrieving student information with email support.

## Main Functions

- **Add Student**: Allows users to add a new student by providing their name and email address.
- **Get Students**: Retrieves and displays a list of all students along with their email addresses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management.git
   cd student-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests
   ```

4. **Run the Database Migration**:
   Before running the application, ensure the database schema is updated to include the new email field:
   ```bash
   python migration.py
   ```

5. **Start the Application**:
   ```bash
   python main.py
   ```

   The application will be running at `http://127.0.0.1:8000`.

## How to Use the Application

1. **Access the Dashboard**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

2. **Add a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to submit the information.
   - A success message will appear if the student is added successfully.

3. **Get Students**:
   - Click the "Get Students" button to retrieve and display the list of all students.
   - The list will show each student's ID, name, and email address.

## Additional Information

- **Database**: The application uses SQLite for storing student records. The database file is `students.db` located in the project directory.
- **API Endpoints**:
  - `POST /students/`: To add a new student.
  - `GET /students/`: To retrieve the list of students.

## Troubleshooting

- If you encounter any issues while running the application, ensure that all dependencies are installed correctly and that the database migration has been executed.
- Check the console for any error messages that may provide insight into what went wrong.

## Support

For further assistance, please reach out to our support team via the contact information provided in the repository.
```

This manual provides a comprehensive overview of the Student Management System, including installation instructions, usage guidelines, and troubleshooting tips. Let me know if you need any further modifications or additions!