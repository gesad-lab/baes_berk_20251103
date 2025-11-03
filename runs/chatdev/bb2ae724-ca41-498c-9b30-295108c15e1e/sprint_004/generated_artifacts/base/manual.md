```markdown
# Course Management API

A simple API for managing students and courses using FastAPI and SQLite.

## Main Functions

This software provides the following functionalities:

- **Create Students**: Allows users to create new student records with a name and email.
- **Retrieve Students**: Enables users to fetch student details by their unique ID.
- **Create Courses**: Allows users to create new course records with a name and level.
- **Database Migration**: Ensures that the database schema is updated to include the Course table while preserving existing Student data.

## Installation of Environment Dependencies

To set up the environment for this application, you need to install the required dependencies. Follow these steps:

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
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Running the API

1. **Start the FastAPI Server**:
   Navigate to the directory where `main.py` is located and run:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

### Using the GUI

1. **Run the GUI Application**:
   In a separate terminal, navigate to the directory where `gui.py` is located and run:
   ```bash
   python gui.py
   ```
   This will open a simple Tkinter GUI for interacting with the API.

### Creating Students

- **Input**: Enter the student's name and email in the respective fields.
- **Action**: Click on the "Create Student" button.
- **Output**: The application will display a success message with the created student's name or an error message if the creation fails.

### Creating Courses

- **Input**: Enter the course name and level in the respective fields.
- **Action**: Click on the "Create Course" button.
- **Output**: The application will display a success message with the created course's name or an error message if the creation fails.

### Database Migration

To ensure that the Course table is created without losing existing Student data, run the migration script:
```bash
python migration.py
```

This script will check for the existence of the Student table and create the Course table accordingly.

## Documentation

For more detailed information on FastAPI, SQLAlchemy, and Pydantic, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

Feel free to reach out for any support or questions regarding the application!
```