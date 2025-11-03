Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management Application

A comprehensive application for managing students, courses, and teachers, allowing for seamless relationships between these entities.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Teacher Management**: Create, read, update, and delete teacher records.
- **Relationships**: Assign teachers to courses and manage student enrollments in courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

Before running the application, ensure that the database is set up correctly:

1. **Run the migration script** to create the necessary tables and columns:
   ```bash
   python main.py
   ```

This script will create the `students`, `courses`, and `teachers` tables, as well as add the `teacher_id` column to the `courses` table while preserving existing data.

## How to Use the Application

1. **Start the application**:
   ```bash
   python main.py
   ```

2. **Access the GUI**:
   The graphical user interface (GUI) is currently under development and will be available in `gui.py`. For now, you can interact with the application through the command line or by extending the GUI code.

3. **Managing Entities**:
   - **Students**: Use the provided functions to add new students, view existing students, and enroll them in courses.
   - **Courses**: Create new courses and assign teachers to them using the `teacher_id` field.
   - **Teachers**: Add new teachers and link them to courses.

## Example Usage

- **Creating a New Student**:
   ```python
   new_student = StudentCreate(name="John Doe", email="john.doe@example.com")
   ```

- **Creating a New Course with a Teacher**:
   ```python
   new_course = CourseCreate(name="Mathematics", level="Beginner", teacher_id=1)
   ```

- **Assigning a Teacher to a Course**:
   When creating or updating a course, specify the `teacher_id` to link the course with the teacher.

## Documentation

For more detailed documentation, including API references and advanced usage examples, please refer to the following resources:

- [API Documentation](https://your-api-docs-link)
- [Getting Started Guide](https://your-getting-started-guide-link)
- [Example Use Cases](https://your-example-use-cases-link)

## Support

If you encounter any issues or have questions, please reach out to our support team via [support@yourcompany.com](mailto:support@yourcompany.com).

---

Thank you for using the Student Course Management Application! We hope it helps you manage your educational entities effectively.
```

This manual provides a comprehensive overview of the application, installation instructions, usage examples, and support information, ensuring that users can effectively utilize the software.