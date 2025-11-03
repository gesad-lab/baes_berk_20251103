Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management System

A simple application for managing students and their course enrollments.

## Main Functions

- **Add Student**: Create a new student entry with their name, email, and associated course IDs.
- **Manage Courses**: Create and manage courses that students can enroll in.
- **View Students**: Retrieve a list of students along with their enrolled courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi[all] sqlalchemy
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## 🤔 What is this?

The Student Management System is designed to help educational institutions manage student records and their course enrollments efficiently. It allows users to add students, manage courses, and view student-course relationships.

## 📖 How to Use

### Adding a Student

1. **Open the GUI**:
   The application provides a simple graphical user interface (GUI) built with Tkinter.

2. **Fill in the Student Details**:
   - **Student Name**: Enter the name of the student.
   - **Student Email**: Enter the email address of the student.
   - **Course IDs**: Enter the IDs of the courses the student is enrolling in, separated by commas.

3. **Submit**:
   Click the "Add Student" button to submit the information. A success message will appear if the student is added successfully.

### Managing Courses

To add courses, you can use the `/courses` API endpoint. Here’s how to do it:

1. **Send a POST Request**:
   Use a tool like Postman or cURL to send a request to the API:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
   ```

2. **Check the Response**:
   The response will contain the details of the created course.

### Viewing Students

To view all students and their enrolled courses, you can access the `/students` endpoint via a GET request:
```bash
curl -X GET "http://127.0.0.1:8000/students"
```

## 📚 Documentation

For more detailed documentation, including API references and advanced usage, please refer to the following sections:

- [Getting Started](https://fastapi.tiangolo.com/tutorial/)
- [API Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)

## 🛠️ Troubleshooting

If you encounter any issues while running the application, consider the following:

- Ensure that all dependencies are installed correctly.
- Check the console for any error messages.
- Make sure the database is accessible and the tables are created.

For further assistance, feel free to reach out to our support team.
```

This manual provides a comprehensive overview of the software, installation instructions, usage guidelines, and links to additional resources. Let me know if you need any modifications or additional sections!