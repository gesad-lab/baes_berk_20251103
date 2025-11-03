```markdown
# Student Management System

A simple application for managing students and courses, allowing users to add and view students and courses, and establish relationships between them.

## Main Functions

- **Add Student**: Allows users to add a new student by providing their name and email.
- **View Students**: Displays a list of all registered students along with their details.
- **Add Course**: Enables users to add a new course by specifying its name and level.
- **View Courses**: Shows a list of all available courses with their details.
- **Course Enrollment**: Students can be enrolled in multiple courses, establishing a many-to-many relationship between students and courses.

## Installation

To run the Student Management System, you need to set up your environment and install the required dependencies. Follow these steps:

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
   Make sure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can manually install the necessary packages:
   ```bash
   pip install fastapi sqlalchemy pydantic requests tkinter
   ```

4. **Run the Application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

## How to Use the Application

1. **Open the GUI**:
   After starting the server, run the GUI application:
   ```bash
   python main.py
   ```

2. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student.

3. **Viewing Students**:
   - Click the "View Students" button to display a list of all students.

4. **Adding a Course**:
   - Enter the course name in the "Enter Course Name" field.
   - Enter the course level in the "Enter Course Level" field.
   - Click the "Add Course" button to save the course.

5. **Viewing Courses**:
   - Click the "View Courses" button to display a list of all courses.

6. **Enrolling Students in Courses**:
   - This functionality can be implemented in future updates. Currently, students can be added and courses can be created, but the enrollment feature is not yet available in the GUI.

## Future Enhancements

- Implementing the ability to enroll students in courses directly from the GUI.
- Adding user authentication for better security.
- Enhancing the GUI with more features and improved user experience.

## Conclusion

This Student Management System is a basic application that allows users to manage students and courses effectively. With the outlined steps, you can set up the environment, run the application, and start using its features. For any issues or feature requests, please reach out to the development team.

```
