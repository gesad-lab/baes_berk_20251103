Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Course Management Application

Manage students and their associated courses with ease using our Student Course Management Application. This application allows you to create, retrieve, and update student and course information, as well as manage the relationships between them.

## Main Functions

- **Create Students**: Add new students to the database with their name and email.
- **Retrieve Students**: Fetch a list of all students in the database.
- **Create Courses**: Add new courses with their name and level.
- **Retrieve Courses**: Fetch a list of all courses available in the database.
- **Associate Courses with Students**: Update a student's record to include their enrolled courses.

## Installation Instructions

To get started with the Student Course Management Application, you need to install the necessary dependencies. Follow the steps below:

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Once you have installed the dependencies, you can run the application using the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

## Using the Application

### API Endpoints

You can interact with the application using the following API endpoints:

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Students**:
  - **Endpoint**: `GET /students/`

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

- **Add Courses to a Student**:
  - **Endpoint**: `PUT /students/{student_id}/courses/`
  - **Request Body**:
    ```json
    {
      "course_ids": [1, 2, 3]
    }
    ```

### Example Usage with cURL

Here are some example commands using `curl` to interact with the API:

1. **Create a Student**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

2. **Get All Students**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/students/"
   ```

3. **Create a Course**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
   ```

4. **Add Courses to a Student**:
   ```bash
   curl -X PUT "http://127.0.0.1:8000/students/1/courses/" -H "Content-Type: application/json" -d '{"course_ids": [1, 2]}'
   ```

## Conclusion

This application provides a simple yet powerful way to manage students and their courses. For further information, please refer to the API documentation provided by FastAPI at `http://127.0.0.1:8000/docs` once the application is running.

Feel free to reach out for any support or questions regarding the application!
```

This manual provides a comprehensive overview of the application, guiding users through installation, usage, and interaction with the API.