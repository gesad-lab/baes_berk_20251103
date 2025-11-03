```markdown
# Student Management Application

A comprehensive application for managing students, courses, and teachers. This software allows users to add and view students, courses, and teachers, while maintaining relationships between these entities.

## Main Functions

- **Student Management**: Add, view, and manage student information including name and email.
- **Course Management**: Add, view, and manage courses, including the ability to assign a teacher to each course.
- **Teacher Management**: Add, view, and manage teacher information including name and email.
- **Relationships**: Establish relationships between students and courses, as well as between courses and teachers.

## Installation

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

3. **Install Required Dependencies**:
   You can install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can manually install the necessary packages:
   ```bash
   pip install fastapi sqlalchemy alembic requests tkinter
   ```

4. **Set Up the Database**:
   The application uses SQLite for the database. You can create the database by running the following command:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

5. **Run Database Migrations**:
   To apply the database migrations, run:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the Application**:
   Run the application using the following command:
   ```bash
   python main.py
   ```

2. **Access the GUI**:
   The application will launch a graphical user interface (GUI) where you can manage students, courses, and teachers.

3. **Managing Students**:
   - **Add Student**: Enter the student's name and email, then click "Add Student".
   - **View Students**: Click "View Students" to see the list of all students.

4. **Managing Courses**:
   - **Add Course**: Enter the course name, level, and the teacher ID, then click "Add Course".
   - **View Courses**: Click "View Courses" to see the list of all courses along with their assigned teacher IDs.

5. **Managing Teachers**:
   - **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".
   - **View Teachers**: Click "View Teachers" to see the list of all teachers.

## Additional Information

- **Database Schema**: The application maintains a relational database schema that includes tables for students, courses, and teachers, with appropriate foreign key relationships.
- **Data Preservation**: The database migration process ensures that existing data for students, courses, and teachers is preserved during updates.

For further assistance or to report issues, please contact the support team.
```