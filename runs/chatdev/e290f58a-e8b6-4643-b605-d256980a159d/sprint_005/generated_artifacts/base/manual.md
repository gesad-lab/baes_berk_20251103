Here's a detailed user manual for the software, including the main functions, installation instructions, and usage guidelines.

```markdown
# Student-Course Management System

A comprehensive application for managing student and course relationships, allowing students to enroll in multiple courses and track their progress.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Enrollment**: Associate students with multiple courses through a many-to-many relationship.
- **Data Persistence**: All data is stored in a SQLite database, ensuring data integrity and persistence.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy pydantic
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## 🤔 What is this?

The Student-Course Management System is designed to facilitate the management of students and their course enrollments. It allows users to create and manage student and course records, as well as track which students are enrolled in which courses.

### Key Features:

- **Create Students**: Add new students with their names and email addresses.
- **Create Courses**: Add new courses with names and levels.
- **Enroll Students in Courses**: Associate students with multiple courses through a many-to-many relationship.
- **Data Migration**: The application supports database migrations to preserve existing data during updates.

## 📖 Documentation

For more detailed information on how to use the application, please refer to the following sections:

### Getting Started

- **Installation**: Follow the Quick Install section above to set up the environment.
- **Running the Application**: Use the command provided to start the FastAPI application.

### How-To Examples

- **Creating a Student**:
  Send a POST request to `/students` with the following JSON body:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Creating a Course**:
  Send a POST request to `/courses` with the following JSON body:
  ```json
  {
    "name": "Mathematics",
    "level": "Beginner"
  }
  ```

- **Enrolling a Student in a Course**:
  Update a student record to include course IDs in the `courses` field.

### Reference

- **API Endpoints**:
  - `POST /students`: Create a new student.
  - `GET /students`: Retrieve all students.
  - `POST /courses`: Create a new course.
  - `GET /courses`: Retrieve all courses.

### Resources

For further reading and resources, please refer to the official FastAPI documentation: [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

This manual provides a comprehensive overview of the Student-Course Management System, guiding users through installation, usage, and available features.
``` 

Feel free to modify any sections as needed or add additional information that may be relevant to the users.