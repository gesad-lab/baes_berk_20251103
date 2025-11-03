Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher and Student Registration Dashboard

A simple GUI application for managing teacher and student registrations, built using Python and FastAPI.

## Main Functions

This application allows users to:
- Register new students with their name, email, and associated courses.
- Register new teachers with their name and email.
- Store and manage data in a SQLite database.
- Provide a user-friendly interface for data entry.

## Quick Install

To set up the environment and run the application, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic requests
   ```

4. **Run the database migration:**
   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Run the GUI application:**
   ```bash
   python gui.py
   ```

## How to Use the Application

### 1. Registering a Student

- Open the application.
- Fill in the **Student Name**, **Student Email**, and **Courses** (comma-separated).
- Click the **Submit Student** button.
- A confirmation message will appear if the registration is successful.

### 2. Registering a Teacher

- In the same application window, locate the **Teacher Registration** section.
- Fill in the **Teacher Name** and **Teacher Email**.
- Click the **Submit Teacher** button.
- A confirmation message will appear if the registration is successful.

### 3. Viewing Registered Data

- The application currently does not provide a direct way to view registered data through the GUI.
- You can access the database directly using a SQLite viewer or by querying the API endpoints:
  - **Students:** `GET http://127.0.0.1:8000/students`
  - **Teachers:** `GET http://127.0.0.1:8000/teachers`

## API Documentation

For more advanced usage, you can interact with the API directly. The following endpoints are available:

- **POST /students**
  - Request Body: `{ "name": "string", "email": "string", "courses": ["string"] }`
  - Response: Returns the created student object.

- **POST /teachers**
  - Request Body: `{ "name": "string", "email": "string" }`
  - Response: Returns the created teacher object.

## Additional Information

- The application uses SQLite as the database backend, which is lightweight and easy to set up.
- The database schema includes tables for students, teachers, and courses, ensuring data integrity and relationships.
- The application is built using FastAPI, which provides automatic interactive API documentation at `http://127.0.0.1:8000/docs`.

## Conclusion

This application serves as a basic framework for managing student and teacher registrations. It can be extended with additional features such as data visualization, reporting, and more complex relationships between entities.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and additional information to help users effectively utilize the software.