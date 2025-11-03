```markdown
# Student Course Management Application

This application allows users to manage students and their associated courses. It provides a user-friendly interface for creating and managing student records, as well as the courses they are enrolled in.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Enrollment**: Associate students with courses, allowing for a many-to-many relationship between students and courses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install sqlalchemy pydantic
   ```

4. **Run the Application**:
   Ensure that you have SQLite installed, as the application uses SQLite for the database. Then, run the main script to create the necessary tables and start the application:
   ```bash
   python main.py
   ```

## Usage

Once the application is running, you can interact with it through the graphical user interface (GUI) provided in `gui.py`. Here’s how to use the main features:

### Adding a Student

1. Navigate to the "Add Student" section in the dashboard.
2. Fill in the student's name and email address.
3. Click the "Submit" button to create the student record.

### Adding a Course

1. Navigate to the "Add Course" section in the dashboard.
2. Fill in the course name and level.
3. Click the "Submit" button to create the course record.

### Enrolling a Student in a Course

1. Navigate to the "Enroll Student" section.
2. Select a student from the dropdown list.
3. Select one or more courses from the available options.
4. Click the "Enroll" button to associate the student with the selected courses.

### Viewing Students and Their Courses

1. Navigate to the "View Students" section.
2. You will see a list of all students along with their enrolled courses.

### Updating and Deleting Records

- To update a student or course, select the record you wish to modify and make the necessary changes.
- To delete a student or course, select the record and click the "Delete" button.

## Database Migration

The application includes a migration script that ensures existing data is preserved while updating the database schema. The `main.py` script creates the necessary tables and adds the email column to the students table if it does not already exist.

## Conclusion

This Student Course Management Application provides a comprehensive solution for managing students and their courses. With its intuitive interface and robust backend, users can easily maintain records and track student enrollments.
```
