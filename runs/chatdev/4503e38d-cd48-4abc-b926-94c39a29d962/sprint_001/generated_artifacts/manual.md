Here's the `manual.md` file for the web application that we developed, which includes instructions on installation, usage, and an overview of the main functions.

```markdown
# Student Registration Web Application

A simple web application for managing student registrations using FastAPI and SQLite.

## Overview

This application allows users to register students by providing their names. The application exposes a RESTful API for creating and retrieving student records. The data is stored in an SQLite database, which is automatically created on startup.

### Main Functions

- **Register a Student**: Users can submit a student's name, which will be stored in the database.
- **View Student Records**: The application can be extended to retrieve and display student records (not implemented in the current version).

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository** (if applicable):
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

## Running the Application

1. **Start the FastAPI Server**:
   Run the following command in the terminal:
   ```bash
   python main.py
   ```
   The server will start and listen on `http://127.0.0.1:8000`.

2. **Access the API**:
   You can interact with the API using tools like Postman or curl. The endpoint to register a student is:
   ```
   POST http://127.0.0.1:8000/students
   ```
   The request body should be in JSON format:
   ```json
   {
       "name": "John Doe"
   }
   ```

3. **Using the GUI**:
   The application also includes a simple GUI built with Tkinter. To run the GUI, execute:
   ```bash
   python gui.py
   ```
   This will open a window where you can enter a student's name and submit it.

## Example Usage

1. **Register a Student via API**:
   Using curl, you can register a student like this:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students" -H "Content-Type: application/json" -d '{"name": "Jane Doe"}'
   ```

2. **Register a Student via GUI**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Submit" button to register the student.

## Additional Information

- **Database**: The application uses SQLite for data persistence. The database file `students.db` will be created in the same directory as the application.
- **CORS**: The application allows cross-origin requests, making it suitable for frontend applications hosted on different domains.

## Documentation

For more detailed information about FastAPI, SQLAlchemy, and Pydantic, please refer to their official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Support

If you encounter any issues or have questions, please reach out to the support team or consult the documentation linked above.

Happy coding!
```

This manual provides a comprehensive guide for users to understand the application, install it, and use its features effectively.