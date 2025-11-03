Here's a detailed user manual for the Student application, formatted in Markdown:

```markdown
# Student Application

A simple application for managing student records, including their names and email addresses.

## Main Functions

The Student Application allows users to:

- Add new students with their names and email addresses.
- View confirmation messages upon successful submission.
- Handle errors gracefully during the submission process.

## Quick Install

To run the Student Application, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic requests tkinter alembic
```

## 🤔 What is this?

The Student Application is designed to manage student records efficiently. It allows users to input student names and email addresses, which are then stored in a SQLite database. The application also includes a graphical user interface (GUI) built with Tkinter for easy interaction.

## 📖 How to Use the Application

1. **Run the Application:**
   To start the application, execute the `main.py` file. You can do this by running the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Enter Student Information:**
   - A window will appear prompting you to enter the student's name and email address.
   - Fill in the required fields.

3. **Submit the Student Data:**
   - Click the "Submit" button to send the data to the backend.
   - If the submission is successful, a confirmation message will be displayed with the student's name.
   - If there is an error (e.g., network issues), an error message will be shown.

4. **Database Migration:**
   - The application includes a migration script to add the email field to the existing student records.
   - To apply the migration, run the following command:

   ```bash
   alembic upgrade head
   ```

   This will add the email column to the `students` table while preserving existing data.

## 🛠️ Development Notes

- The application uses SQLAlchemy for database interactions and Pydantic for data validation.
- The database is set up to use SQLite, which is lightweight and easy to manage.
- The GUI is built using Tkinter, providing a simple interface for user interaction.

## 📄 Documentation

For more detailed information on the code structure and functionality, refer to the following files:

- `schemas.py`: Defines the Pydantic schemas for request and response validation.
- `database.py`: Handles the database connection and session management.
- `models.py`: Defines the SQLAlchemy model for the Student entity.
- `migration.py`: Contains the migration script to add the email column to the existing students table.

For further assistance or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the Student application, including installation instructions, usage guidelines, and development notes. Let me know if you need any modifications or additional information!