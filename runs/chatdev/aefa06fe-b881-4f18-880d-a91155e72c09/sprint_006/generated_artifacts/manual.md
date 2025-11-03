```markdown
# Teacher Management Application

A simple application for managing teachers, courses, and students in an educational environment.

## Main Functions

The Teacher Management Application allows users to:

- Create and manage teacher profiles.
- Associate teachers with courses.
- Manage student enrollments in courses.
- View and retrieve information about teachers, courses, and students.

## Installation

To run the Teacher Management Application, you need to install the required environment dependencies. Follow the steps below:

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**
   You can install the required packages using pip:
   ```bash
   pip install sqlalchemy alembic pydantic tkinter
   ```

4. **Database Setup:**
   The application uses SQLite as the database. The database will be created automatically when you run the migration script.

## How to Use the Application

### Running the Application

1. **Run the Migration Script:**
   Before using the application, you need to run the migration script to set up the database schema.
   ```bash
   alembic upgrade head
   ```

2. **Start the Application:**
   Run the main application file to launch the GUI:
   ```bash
   python main.py
   ```

### Using the GUI

- **Creating a Teacher:**
  - Enter the teacher's name and email in the provided fields.
  - Click the "Create Teacher" button to save the teacher's information.

- **Managing Courses and Students:**
  - The GUI currently focuses on teacher management. Future updates will include functionalities for managing courses and student enrollments.

### Database Schema

The application uses the following database schema:

- **Teachers Table:**
  - `id`: Integer, Primary Key
  - `name`: String, Not Null
  - `email`: String, Not Null

- **Courses Table:**
  - `id`: Integer, Primary Key
  - `name`: String, Not Null
  - `level`: String, Not Null
  - `teacher_id`: Integer, Foreign Key referencing Teachers

- **Students Table:**
  - `id`: Integer, Primary Key
  - `name`: String, Not Null
  - `email`: String, Not Null

- **Student Courses Association Table:**
  - `student_id`: Integer, Foreign Key referencing Students
  - `course_id`: Integer, Foreign Key referencing Courses

## Future Enhancements

- Implement functionalities for managing courses and student enrollments.
- Add validation and error handling in the GUI.
- Provide a way to view existing teachers, courses, and students.

## Support

For any issues or feature requests, please contact the development team at support@chatdev.com.

```
