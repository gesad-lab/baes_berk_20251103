```markdown
# ChatDev Teacher Management System

Welcome to the ChatDev Teacher Management System! This software allows you to manage teachers, students, and courses efficiently. Below is a detailed user manual that covers the main functions of the software, installation instructions, and usage guidelines.

## Main Functions

1. **Manage Teachers**: 
   - Create, retrieve, and list teachers with their names and email addresses.
   
2. **Manage Students**: 
   - Create, retrieve, and list students along with their associated courses.
   
3. **Manage Courses**: 
   - Create, retrieve, and list courses along with their associated students.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev-teacher-management.git
   cd chatdev-teacher-management
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

4. **Set Up the Database**:
   - Ensure you have SQLite installed (it comes pre-installed with Python).
   - Run the following command to apply database migrations:
   ```bash
   alembic upgrade head
   ```

## How to Use the Software

### Starting the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

You can interact with the application using the following API endpoints:

#### Teacher Management

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Teachers**:
  - **Endpoint**: `GET /teachers/`
  - **Response**: List of teachers with their details.

#### Student Management

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com",
      "course_ids": [1, 2]
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: List of students with their details.

#### Course Management

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: List of courses with their details.

## Conclusion

This software provides a robust solution for managing teachers, students, and courses. By following the instructions above, you can easily set up the environment and start using the application. For further assistance, please refer to the code documentation or reach out to our support team.

Happy coding!
```