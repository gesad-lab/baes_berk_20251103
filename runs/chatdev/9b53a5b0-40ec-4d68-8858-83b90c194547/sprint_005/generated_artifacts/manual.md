```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers. This software allows users to add, view, and manage teacher entities along with existing student and course data.

## Main Functions

- **Add Student**: Allows users to input student details (name and email) and store them in the database.
- **View Students**: Displays a list of all registered students along with their details.
- **Add Course**: Enables users to create new courses by providing course name and level.
- **View Courses**: Lists all available courses in the system.
- **Add Teacher**: Users can add new teachers by entering their name and email.
- **View Teachers**: Displays a list of all registered teachers.

## Installation and Environment Setup

To run the Teacher Management System, you need to set up your environment and install the required dependencies. Follow these steps:

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

3. **Install Required Dependencies**:
   Make sure you have `pip` installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can manually install the necessary packages:
   ```bash
   pip install sqlalchemy pydantic fastapi requests
   ```

4. **Run Database Migration**:
   Before running the application, ensure that the database is set up correctly. You can run the migration script to create the necessary tables:
   ```bash
   python -c "from database import migrate_database; migrate_database()"
   ```

5. **Start the Application**:
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

1. **Open the Application**:
   Launch the GUI application by running:
   ```bash
   python main.py
   ```

2. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click on "Add Student" to save the information.

3. **Viewing Students**:
   - Click on "View Students" to see the list of all registered students.

4. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Click on "Add Course" to save the information.

5. **Viewing Courses**:
   - Click on "View Courses" to see the list of all available courses.

6. **Adding Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click on "Add Teacher" to save the information.

7. **Viewing Teachers**:
   - Click on "View Teachers" to see the list of all registered teachers.

## Conclusion

This Teacher Management System provides a simple interface for managing students, courses, and teachers. It is designed to be user-friendly and efficient, making it easy to keep track of educational entities. For further enhancements or features, feel free to contribute or reach out for support.
```