Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management Application

Manage courses and students efficiently with our Course Management Application. This software allows you to create and manage courses, ensuring that all necessary data is stored and accessible.

## Main Functions

- **Create Course**: Add new courses with a specified name and level.
- **Manage Students**: Maintain student records, including their names and emails.
- **Database Management**: Automatically handle database migrations to ensure data integrity.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
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
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

Ensure you have the following dependencies installed:

- **SQLAlchemy**: The ORM used for database interactions.
- **Pydantic**: For data validation and settings management using Python type annotations.

### Example `requirements.txt`:
```
SQLAlchemy==1.4.22
pydantic==1.8.2
```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing the main script:
   ```bash
   python main.py
   ```

2. **Creating a Course**:
   To create a new course, you can use the provided API endpoints or extend the GUI in `gui.py` (currently empty). The course creation requires the following fields:
   - `name`: The name of the course (string, required).
   - `level`: The level of the course (string, required).

3. **Database Migration**:
   The application automatically handles database migrations. When you run `main.py`, it will create the necessary tables and ensure that existing student data is preserved.

4. **Accessing Student Data**:
   You can manage student records through the application. Each student has a name and an email, and you can extend this functionality as needed.

## Additional Notes

- If you are using SQLite, you do not need to include it in the `requirements.txt` file, as it is part of Python's standard library.
- Ensure that your Python version is compatible with the dependencies listed.

## Documentation

For more detailed documentation, including API references and advanced usage, please refer to the [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) and [Pydantic Documentation](https://pydantic-docs.helpmanual.io/).

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact information provided in the repository.

Happy coding!
```

This manual provides a comprehensive overview of the application, installation instructions, and usage guidelines, ensuring that users can effectively utilize the software.