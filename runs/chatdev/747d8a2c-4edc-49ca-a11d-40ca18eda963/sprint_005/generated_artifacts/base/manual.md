```markdown
# Student Course Enrollment System

A simple application to manage students and their course enrollments.

## Main Functions

- **Create Students**: Add new students to the system with their name and email.
- **Create Courses**: Add new courses with a name and level.
- **Enroll Students in Courses**: Enroll existing students in available courses.
- **Retrieve Students**: Get a list of all students in the system.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-enrollment.git
   cd student-course-enrollment
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic
   ```

4. **Install Tkinter** (if you plan to use the GUI):
   - For Windows, Tkinter is included with Python installations.
   - For Ubuntu, you can install it using:
     ```bash
     sudo apt-get install python3-tk
     ```

## Database Setup

1. **Create the Database**:
   Run the following command to create the SQLite database and the necessary tables:
   ```bash
   python -c "from database import create_database; create_database()"
   ```

2. **Run Migrations**:
   To apply the latest database migrations, run:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

### API Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john@example.com"
    }
    ```

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Enroll a Student in a Course**:
  - **Endpoint**: `POST /students/{student_id}/courses/{course_id}`
  - **Example**: To enroll student with ID 1 in course with ID 2.

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (optional), `limit` (optional)

### GUI Usage

1. **Run the GUI**:
   To start the GUI application, run:
   ```bash
   python gui.py
   ```

2. **Interact with the GUI**:
   - Use the interface to create students and courses.
   - Enroll students in courses through the GUI.

## Conclusion

This application provides a simple way to manage students and their course enrollments. By following the installation and usage instructions, you can quickly set up and start using the system. For any issues or feature requests, feel free to reach out to the development team.
```