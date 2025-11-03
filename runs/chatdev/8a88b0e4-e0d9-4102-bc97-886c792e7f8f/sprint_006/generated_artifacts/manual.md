Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Application

A comprehensive application for managing students, courses, and teachers, designed to facilitate educational administration and enhance learning experiences.

## Main Functions

The Student Application includes the following key functionalities:

- **Student Management**: Create, read, update, and delete student records, including their associated courses.
- **Course Management**: Manage courses, including their names, levels, and associated teachers.
- **Teacher Management**: Create and manage teacher records, ensuring they can be linked to courses.
- **Relationships**: Establish relationships between students, courses, and teachers, allowing for a more integrated educational experience.

## Quick Install

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
   pip install -r requirements.txt
   ```

## Database Setup

The application uses SQLite as its database. The initial setup will create the necessary tables for students, courses, and teachers.

1. **Run the Migration Script**:
   After installing the dependencies, run the following command to create the database tables and apply migrations:
   ```bash
   python main.py
   ```

## Usage

### Running the Application

To start using the application, you can run the main script:

```bash
python main.py
```

### API Endpoints

The application exposes several API endpoints for managing students, courses, and teachers. Below are some examples of how to interact with the API:

- **Create a Student**:
  ```http
  POST /students
  Content-Type: application/json

  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```

- **Create a Course**:
  ```http
  POST /courses
  Content-Type: application/json

  {
      "name": "Mathematics",
      "level": "Intermediate",
      "teacher_id": 1  # ID of the teacher
  }
  ```

- **Create a Teacher**:
  ```http
  POST /teachers
  Content-Type: application/json

  {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
  }
  ```

### Data Relationships

- Each course can have one teacher associated with it.
- Students can enroll in multiple courses, and courses can have multiple students.

### GUI

The application includes a graphical user interface (GUI) for easier interaction. You can run the GUI by executing:

```bash
python gui.py
```

## Conclusion

This Student Application provides a robust framework for managing educational data. By following the installation and usage instructions, you can effectively manage students, courses, and teachers, enhancing the educational experience for all users.

For further assistance or feature requests, please contact the support team.
```

This manual provides a comprehensive overview of the software, guiding users through installation, setup, and usage, while also highlighting the application's main functions.