```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. You can add, view, and enroll students in courses, as well as manage teacher information.

## Main Functions

- **Manage Students**: Add new students and view existing students.
- **Manage Courses**: Create new courses, view existing courses, and associate them with teachers.
- **Manage Teachers**: Add new teachers and view existing teachers.
- **Enroll Students**: Enroll students in courses.

## Quick Install

To set up the environment and run the application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-course-management.git
   cd chatdev-course-management
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

4. **Run Database Migration**:
   Before running the application, ensure that the database is set up correctly:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Start the Application**:
   Run the GUI application by executing:
   ```bash
   python gui.py
   ```

2. **Manage Students**:
   - **Add Student**: Enter the student's name and email, then click "Add Student".
   - **View Students**: Click "Get Students" to see the list of all students.

3. **Manage Courses**:
   - **Add Course**: Enter the course name, level, and teacher ID (if applicable), then click "Add Course".
   - **View Courses**: Click "Get Courses" to see the list of all courses.

4. **Manage Teachers**:
   - **Add Teacher**: Enter the teacher's name and email, then click "Add Teacher".
   - **View Teachers**: Click "Get Teachers" to see the list of all teachers.

5. **Enroll Students in Courses**:
   - Enter the student ID and course ID, then click "Enroll Student in Course".

## Database Schema

The application uses SQLite as the database and includes the following entities:
- **Student**: Represents students with attributes like ID, name, email, and associated courses.
- **Course**: Represents courses with attributes like ID, name, level, and associated teacher.
- **Teacher**: Represents teachers with attributes like ID, name, and email.

## Additional Information

- The application is built using Python and utilizes Tkinter for the GUI.
- The database schema has been updated to include a relationship between courses and teachers, ensuring that each course can have a designated teacher.

For any issues or further assistance, please contact our support team.

Happy managing!
```