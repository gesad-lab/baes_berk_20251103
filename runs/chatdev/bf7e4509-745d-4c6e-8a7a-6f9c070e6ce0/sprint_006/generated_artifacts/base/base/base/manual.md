```markdown
# Student and Course Management Application

This application allows users to manage students and courses through a simple API and GUI interface. Users can create, retrieve, and manage student and course data efficiently.

## Main Functions

- **Student Management**: Create and retrieve student records, including their names and email addresses.
- **Course Management**: Create and retrieve course records, including course names and levels.
- **Database Management**: The application uses a SQLite database to store student and course information, ensuring data persistence.

## Installation of Environment Dependencies

To set up the environment for this application, you need to install the required dependencies. Follow the steps below:

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Running the Application

1. **Start the FastAPI server**:
   You can run the API server using Uvicorn. Execute the following command in your terminal:
   ```bash
   uvicorn api:router --reload
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI. Here, you can test the endpoints for creating and retrieving students and courses.

### Using the GUI

1. **Run the GUI application**:
   Execute the following command in your terminal:
   ```bash
   python main.py
   ```
   This will open a Tkinter window for the Student and Course Management application.

2. **Interacting with the GUI**:
   - **Add Students**: Enter the student's name and email, then click the "Add Student" button to create a new student record.
   - **View Students**: Click the "View Students" button to see a list of all students.
   - **Add Courses**: Enter the course name and level, then click the "Add Course" button to create a new course record.
   - **View Courses**: Click the "View Courses" button to see a list of all courses.

### Database Migration

The application includes a migration script to add the Course entity to the database without affecting existing Student data. To apply the migration, run the following command:
```bash
alembic upgrade head
```

## Conclusion

This Student and Course Management Application provides a simple yet effective way to manage educational data. With the combination of a FastAPI backend and a Tkinter GUI, users can easily interact with the system to manage students and courses.

For further assistance or to report issues, please contact the development team.
```