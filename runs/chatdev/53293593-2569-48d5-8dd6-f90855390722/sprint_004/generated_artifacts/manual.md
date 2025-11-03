```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students and their associated courses effectively. Below is a detailed user manual that introduces the main functions of the software, installation instructions, and usage guidelines.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Course Enrollment**: Associate students with multiple courses through a many-to-many relationship.
- **Data Migration**: Migrate existing student and course data while preserving relationships.

## Quick Install

To get started with the ChatDev Course Management System, you need to install the required environment dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic
```

Make sure you have Python installed on your machine. You can check your Python version by running:

```bash
python --version
```

## Setting Up the Environment

1. **Clone the Repository**: Clone the repository containing the source code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Run the installation command mentioned above to install the required packages.

3. **Database Setup**: The application uses SQLite as the database. The database will be automatically created when you run the application for the first time.

## How to Use the Software

### Running the Application

To run the application and perform database migrations, execute the following command:

```bash
python main.py
```

This will create the necessary tables in the SQLite database and migrate any existing data.

### Managing Students and Courses

You can manage students and courses through the following endpoints (assuming you have set up a web framework like FastAPI or Flask):

- **Create a Student**: Send a POST request to `/students` with the student's name and email.
- **Get All Students**: Send a GET request to `/students` to retrieve a list of all students.
- **Create a Course**: Send a POST request to `/courses` with the course name and level.
- **Get All Courses**: Send a GET request to `/courses` to retrieve a list of all courses.
- **Enroll a Student in a Course**: Send a POST request to `/enroll` with the student ID and course ID to associate a student with a course.

### Example Usage

Here’s an example of how to create a student and a course, and then enroll the student in the course:

1. **Create a Student**:

   ```json
   POST /students
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

2. **Create a Course**:

   ```json
   POST /courses
   {
       "name": "Introduction to Programming",
       "level": "Beginner"
   }
   ```

3. **Enroll the Student in the Course**:

   ```json
   POST /enroll
   {
       "student_id": 1,
       "course_id": 1
   }
   ```

## Documentation

For further details on the API endpoints, data models, and advanced usage, please refer to the [API Documentation](https://example.com/api-docs).

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Thank you for using the ChatDev Course Management System! We hope it helps you manage your educational needs effectively.
```