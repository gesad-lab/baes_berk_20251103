```markdown
# Teacher Management System

A simple application for managing students, courses, and teachers using FastAPI and a SQLite database.

## Main Functions

This application allows users to perform the following operations:

- **Create Students**: Add new students with their names and email addresses.
- **Create Courses**: Add new courses with their names and levels.
- **Enroll Students in Courses**: Enroll existing students in specified courses.
- **Create Teachers**: Add new teachers with their names and email addresses.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

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
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   alembic
   ```
   Then, install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Initialize the Database**:
   Before running the application, ensure that the database is initialized. You can do this by running the following command:
   ```bash
   python main.py
   ```

2. **Start the FastAPI Server**:
   Run the following command to start the server:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

3. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

## Using the Application

### GUI Interaction

The application includes a simple GUI built with Tkinter for easier interaction. To use the GUI:

1. **Run the GUI**:
   Execute the following command:
   ```bash
   python gui.py
   ```

2. **Creating Students**:
   - Enter the student's name and email in the respective fields.
   - Click on the "Create Student" button to add the student.

3. **Creating Courses**:
   - Enter the course name and level in the respective fields.
   - Click on the "Create Course" button to add the course.

4. **Enrolling Students in Courses**:
   - Enter the student ID and course details.
   - Click on the "Enroll in Course" button to enroll the student.

5. **Creating Teachers**:
   - Enter the teacher's name and email in the respective fields.
   - Click on the "Create Teacher" button to add the teacher.

### API Interaction

You can also interact with the API directly using tools like Postman or cURL. Here are some example requests:

- **Create a Student**:
  ```http
  POST /students/
  Content-Type: application/json

  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```

- **Create a Course**:
  ```http
  POST /courses/
  Content-Type: application/json

  {
      "name": "Mathematics",
      "level": "Beginner"
  }
  ```

- **Enroll a Student in a Course**:
  ```http
  POST /students/{student_id}/courses/
  Content-Type: application/json

  {
      "name": "Mathematics",
      "level": "Beginner"
  }
  ```

- **Create a Teacher**:
  ```http
  POST /teachers/
  Content-Type: application/json

  {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
  }
  ```

## Conclusion

This Teacher Management System provides a simple yet effective way to manage students, courses, and teachers. By following the installation and usage instructions, you can easily set up and interact with the application. For further customization or enhancements, feel free to explore the codebase and make modifications as needed.
```