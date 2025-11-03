Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management System

A simple application for managing student records, including adding and retrieving student information.

## Main Functions

- **Add Student**: Allows users to add a new student with a name and email address.
- **Get Students**: Fetches and displays a list of all students, including their names and email addresses.

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

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   tkinter
   ```

## Usage

### Running the Application

1. **Start the API**:
   Open a terminal and run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Run the GUI**:
   In another terminal, run the GUI application:
   ```bash
   python gui.py
   ```

### Adding a Student

- In the GUI, enter the student's name and email address in the respective fields.
- Click the "Add Student" button to submit the information.
- A confirmation message will appear indicating whether the student was added successfully.

### Retrieving Students

- Click the "Get Students" button to fetch and display the list of all students.
- The list will show each student's name along with their email address.

## Database Migration

The application includes a migration script that adds the email field to the existing Student table without losing any existing data. To run the migration:

1. Ensure the FastAPI server is not running.
2. Execute the migration script:
   ```bash
   python main.py
   ```

This will check if the email column exists and add it if it does not.

## Additional Information

- The application uses SQLite as the database. The database file is located in the project directory as `students.db`.
- The application is built using Python and utilizes FastAPI for the backend and Tkinter for the GUI.

## Support

For any issues or questions, please reach out to the development team via the support channel or open an issue in the GitHub repository.

```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and support information. Let me know if you need any further modifications or additional sections!