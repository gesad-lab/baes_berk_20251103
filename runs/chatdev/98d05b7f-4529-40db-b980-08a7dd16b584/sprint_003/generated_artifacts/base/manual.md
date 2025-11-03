Here's the detailed user manual for the Student Management application, including installation instructions and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including their names and email addresses.

## Main Functions

- **Add Student**: Allows users to add a new student by entering their name and email address.
- **Fetch Students**: Retrieves and displays a list of all students currently stored in the database.

## Quick Install

To set up the Student Management application, you need to install the required environment dependencies. Follow the steps below:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python**: Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install Required Packages**: Use pip to install the necessary dependencies.
   ```bash
   pip install sqlalchemy requests tkinter
   ```

4. **Set Up the Database**: The application uses SQLite for the database. You can initialize the database by running the following command in your Python environment:
   ```python
   from database import init_db
   init_db()
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing the `main.py` script:
   ```bash
   python main.py
   ```

2. **Adding a Student**:
   - In the GUI, enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the information.

3. **Fetching Students**:
   - Click the "Fetch Students" button to retrieve and display the list of students along with their email addresses.

4. **Viewing Student Records**:
   - The list of students will be displayed in the list box. You can see each student's name and email.

## Additional Information

- The application is built using Python and utilizes the Tkinter library for the graphical user interface.
- The database schema has been updated to include an email field for each student, ensuring that all existing student data is preserved during migration.

## Troubleshooting

- If you encounter issues with database connections, ensure that the SQLite database file (`students.db`) is accessible and that you have the necessary permissions.
- For any errors related to missing packages, double-check that all dependencies are installed correctly.

## Support

For further assistance, please contact the support team at [support@chatdev.com](mailto:support@chatdev.com).

```

This manual provides a comprehensive overview of the Student Management application, guiding users through installation, usage, and troubleshooting.