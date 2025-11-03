```markdown
# Course Management System

A simple application for managing students and courses using FastAPI and SQLite.

## Main Functions

This application provides the following functionalities:

- **Student Management**: Create and manage student records, including their names and emails.
- **Course Management**: Create and manage course records, including course names and levels.
- **Database Persistence**: All data is stored in a SQLite database, ensuring data is preserved across sessions.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: An ASGI server for running FastAPI applications.
- **sqlalchemy**: The ORM (Object Relational Mapper) used for database interactions.
- **pydantic**: Used for data validation and settings management, particularly for request and response schemas.
- **requests**: A library for making HTTP requests, used in the GUI to interact with the API.

Make sure to adjust the versions according to your project's needs or the latest stable releases if necessary.

## How to Use the Application

### Running the API

1. **Start the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

### Interacting with the API

You can interact with the API using tools like Postman, cURL, or through the provided GUI.

#### Using the GUI

1. **Run the GUI application**:
   ```bash
   python gui.py
   ```

2. **Add a Student**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to submit the data.

3. **Add a Course**:
   You can extend the GUI to include functionality for adding courses by creating a similar interface as the student management.

### API Endpoints

- **Create Student**: 
  - **Endpoint**: `POST /students`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Create Course**:
  - **Endpoint**: `POST /courses`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

### Database Migration

The application includes a migration script (`migration.py`) that ensures the Course table is created without affecting existing Student data. You can run this script to apply the migration.

## Conclusion

This Course Management System provides a simple yet effective way to manage students and courses. You can extend its functionality as needed to suit your requirements. For any issues or feature requests, please reach out to the development team.

```
