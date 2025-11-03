```markdown
# Student Course Management Application

A simple application for managing student registrations and course enrollments.

## Main Functions

The Student Course Management Application allows users to:

- **Add Students**: Register new students by providing their name and email.
- **Add Courses**: Create new courses by specifying the course name and level.
- **Enroll Students in Courses**: Enroll registered students in available courses.

## Installation

To run this application, you need to have Python installed on your system. Follow these steps to set up the environment:

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
   You need to install the following dependencies:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic requests tkinter
   ```

4. **Run the Application**:
   Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

5. **Open the GUI**:
   Run the GUI application:
   ```bash
   python gui.py
   ```

## How to Use the Application

### Adding a Student

1. Open the application.
2. Enter the student's name in the "Student Name" field.
3. Enter the student's email in the "Email" field.
4. Click the "Add Student" button.
5. A success message will appear if the student is added successfully.

### Adding a Course

1. Enter the course name in the "Course Name" field.
2. Enter the course level in the "Course Level" field.
3. Click the "Add Course" button.
4. A success message will appear if the course is added successfully.

### Enrolling a Student in a Course

1. Enter the student ID in the "Student ID" field.
2. Enter the course ID in the "Course ID" field.
3. Click the "Enroll Student in Course" button.
4. A success message will appear if the student is enrolled successfully.

### Error Handling

- If you try to add a student or course without filling in the required fields, a warning message will prompt you to enter the necessary information.
- If you attempt to enroll a student in a course that does not exist or if the student is already enrolled in that course, an error message will be displayed.

## Conclusion

This application provides a straightforward interface for managing students and courses. By following the steps outlined in this manual, users can easily navigate through the functionalities and effectively manage their educational data.

For any issues or feature requests, please contact the development team.
```