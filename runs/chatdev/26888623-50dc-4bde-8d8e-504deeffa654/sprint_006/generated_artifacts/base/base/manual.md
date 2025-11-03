```markdown
# Student Course Management Application

This application allows users to manage students and their associated courses. It provides a simple interface to create students, courses, and establish relationships between them.

## Main Functions

- **Create Student**: Add a new student with a name and email.
- **Create Course**: Add a new course with a name and level.
- **Manage Course Relationships**: Associate students with multiple courses and vice versa.

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
   pip install -r requirements.txt
   ```

## How to Use the Application

### 1. Database Setup

Before running the application, ensure that the database is set up correctly. The application uses SQLite for database management.

- The database schema will be automatically created when you run the application for the first time.

### 2. Running the Application

To start the application, run the following command:

```bash
python main.py
```

This will execute the migration script to create the necessary tables in the database.

### 3. Interacting with the Application

You can interact with the application through the GUI (if implemented) or through API endpoints (if using FastAPI). Here are some example API calls:

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
       "level": "Beginner"
   }
   ```

- **Associate a Student with a Course**:
   ```http
   POST /students/{student_id}/courses
   Content-Type: application/json

   {
       "course_id": 1
   }
   ```

### 4. Accessing the Database

The application uses SQLite, and the database file is located at `./students.db`. You can use any SQLite viewer to inspect the data.

## Additional Information

For more detailed documentation, including API references and examples, please refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact form on our website.

```
