Here's a detailed user manual for the Student Management application, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A simple and efficient application for managing student records, including their names and email addresses.

## Main Functions

The Student Management Application allows users to perform the following functions:

- **Create a Student**: Add a new student record with a name and email address.
- **Retrieve Student Information**: Fetch details of existing students.
- **Update Student Information**: Modify the details of a student, including their email.
- **Delete a Student**: Remove a student record from the database.

## Quick Install

To set up the Student Management Application, you need to install the required dependencies. Follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management.git
   cd student-management
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

   Make sure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   alembic
   pydantic
   ```

## Usage

To run the Student Management Application, follow these steps:

1. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   This command will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

2. **Interact with the API**:
   You can use tools like Postman or cURL to interact with the API. Below are some example requests:

   - **Create a Student**:
     ```http
     POST /students
     Content-Type: application/json

     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

   - **Retrieve All Students**:
     ```http
     GET /students
     ```

   - **Update a Student**:
     ```http
     PUT /students/{id}
     Content-Type: application/json

     {
       "name": "John Doe",
       "email": "john.newemail@example.com"
     }
     ```

   - **Delete a Student**:
     ```http
     DELETE /students/{id}
     ```

3. **Database Migration**:
   To apply the database migration that adds the email field to the Student entity, run the following command:
   ```bash
   alembic upgrade head
   ```

   This command will ensure that the database schema is updated while preserving existing student data.

## Conclusion

The Student Management Application is designed to simplify the management of student records. With its easy-to-use API, you can efficiently create, read, update, and delete student information. For further assistance, please refer to the documentation or contact support.
```

This manual provides a comprehensive overview of the application, guiding users through installation and usage while highlighting the main functionalities.