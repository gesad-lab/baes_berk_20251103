```markdown
# Student Course Management System

A simple web application for managing students and their enrolled courses.

## Main Functions

This application allows users to:

- Create new students and courses.
- Retrieve lists of students and courses.
- Enroll students in courses.
- Manage relationships between students and courses through an intuitive API.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/student_course_management.git
   cd student_course_management
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API documentation:**
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by FastAPI.

## 🤔 What is this?

The Student Course Management System is designed to facilitate the management of students and their course enrollments. It provides a RESTful API that allows for easy integration with other systems or front-end applications.

### Key Features:

- **Student Management:** Create and retrieve student records.
- **Course Management:** Create and retrieve course records.
- **Enrollment:** Enroll students in courses, allowing for many-to-many relationships.

## 📖 Usage

### Creating a Student

To create a new student, send a POST request to `/students/` with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Retrieving Students

To retrieve a list of students, send a GET request to `/students/`. You can use query parameters `skip` and `limit` to paginate results.

### Creating a Course

To create a new course, send a POST request to `/courses/` with the following JSON body:

```json
{
  "name": "Mathematics",
  "level": "Beginner"
}
```

### Retrieving Courses

To retrieve a list of courses, send a GET request to `/courses/`. You can also use query parameters `skip` and `limit` for pagination.

### Enrolling a Student in a Course

To enroll a student in a course, send a POST request to `/students/{student_id}/courses/{course_id}`. Replace `{student_id}` and `{course_id}` with the respective IDs of the student and course.

## Database Schema

The application uses SQLite as the database, with the following schema:

- **students**: Contains student records.
- **courses**: Contains course records.
- **student_courses**: An association table that manages the many-to-many relationship between students and courses.

## 🛠️ Development

To contribute to the development of this application, you can fork the repository and submit pull requests. Ensure to follow the coding standards and include tests for new features.

For any issues or feature requests, please open an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
