# Student Management Application

A simple application for managing student records, allowing users to add and view students along with their email addresses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi sqlalchemy alembic requests
   ```

4. **Install a database driver (for SQLite):**
   ```bash
   pip install aiosqlite
   ```

## 🛠️ Main Functions

The Student Management Application provides the following functionalities:

- **Add Student:** Users can add a new student by providing their name and email address.
- **View Students:** Users can view a list of all students along with their details.

## 📖 How to Use the Application

### 1. Run the Application

To start the application, run the following command in your terminal:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

### 2. Using the GUI

Once the server is running, you can launch the GUI application by running:

```bash
python gui.py
```

This will open a window where you can interact with the application.

### 3. Adding a Student

- Enter the student's name in the "Enter Student Name" field.
- Enter the student's email in the "Enter Student Email" field.
- Click the "Add Student" button to submit the information.

If the student is added successfully, a confirmation message will appear in the output area.

### 4. Viewing Students

- Click the "View Students" button to retrieve and display all students in the output area.
- The list will show each student's ID, name, and email address.

## 📦 Database Migration

The application includes a migration script to add the email field to the existing Student entity. To apply the migration, run the following command:

```bash
alembic upgrade head
```

This will update the database schema to include the new email field while preserving existing student data.

## 📄 Documentation

For more detailed documentation on FastAPI and SQLAlchemy, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)

## 🚀 Conclusion

This Student Management Application provides a straightforward interface for managing student records. By following the installation and usage instructions, you can quickly set up and start using the application. If you have any questions or need further assistance, feel free to reach out!