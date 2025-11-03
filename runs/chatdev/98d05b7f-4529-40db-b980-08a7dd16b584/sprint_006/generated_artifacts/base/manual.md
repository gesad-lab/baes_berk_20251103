Here's a detailed user manual for the Teacher Management software, formatted in Markdown:

```markdown
# Teacher Management Software

Manage teachers, students, and courses efficiently with our Teacher Management Software. This application allows you to add and fetch information about teachers, students, and courses seamlessly.

## Main Functions

- **Add Teacher**: Input the teacher's name and email to create a new teacher record.
- **Fetch Teachers**: Retrieve and display a list of all teachers in the system.
- **Add Student**: Input the student's name and email to create a new student record.
- **Fetch Students**: Retrieve and display a list of all students in the system.
- **Add Course**: Input the course name and level, and associate it with a student.
- **Fetch Courses**: Retrieve and display a list of all courses in the system.

## Installation Instructions

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
   Create a `requirements.txt` file with the following content:
   ```
   SQLAlchemy
   requests
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Software

1. **Run the Application**:
   Start the FastAPI server by running the following command in your terminal:
   ```bash
   uvicorn main:app --reload
   ```

2. **Launch the GUI**:
   Open another terminal window and run:
   ```bash
   python main.py
   ```

3. **Interacting with the Application**:
   - **Adding a Teacher**:
     - Enter the teacher's name and email in the respective fields.
     - Click on the "Add Teacher" button to save the information.
   - **Fetching Teachers**:
     - Click on the "Fetch Teachers" button to display a list of all teachers.
   - **Adding a Student**:
     - Enter the student's name and email in the respective fields.
     - Click on the "Add Student" button to save the information.
   - **Fetching Students**:
     - Click on the "Fetch Students" button to display a list of all students.
   - **Adding a Course**:
     - Enter the course name and level, and select a student from the list.
     - Click on the "Add Course" button to save the information.
   - **Fetching Courses**:
     - Click on the "Fetch Courses" button to display a list of all courses.

## Conclusion

This Teacher Management Software provides a user-friendly interface for managing teachers, students, and courses. By following the installation and usage instructions, you can easily set up and operate the application to meet your educational management needs.

For any issues or feature requests, please contact our support team.
```

This manual provides a comprehensive overview of the software, including installation steps, main functionalities, and usage instructions, ensuring that users can effectively utilize the application.