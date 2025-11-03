```markdown
# Course Management Application

A simple application for managing students and courses using FastAPI and SQLAlchemy.

## Main Functions

This application provides the following functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically migrates the database schema to include the new Course table while preserving existing Student data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd student_app
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

## 🤔 What is this?

This application allows users to manage students and courses efficiently. It leverages FastAPI for building the API and SQLAlchemy for ORM (Object Relational Mapping) to interact with the SQLite database.

### Key Features

- **Create Student**: Add new students to the database.
- **Retrieve Students**: Get a list of all students.
- **Create Course**: Add new courses with a name and level.
- **Retrieve Courses**: Get a list of all courses.

## 📖 Usage

### Running the Application

To run the application, execute the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API at `http://127.0.0.1:8000`.

### API Endpoints

- **Students**
  - `POST /students/`: Create a new student. Requires a JSON body with `name` and `email`.
  - `GET /students/`: Retrieve all students.

- **Courses**
  - `POST /courses/`: Create a new course. Requires a JSON body with `name` and `level`.
  - `GET /courses/`: Retrieve all courses.

### Example Requests

#### Create a Student

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
```

#### Create a Course

```bash
curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
```

#### Retrieve Students

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

#### Retrieve Courses

```bash
curl -X GET "http://127.0.0.1:8000/courses/"
```

## Conclusion

This application provides a straightforward way to manage students and courses. With FastAPI's performance and SQLAlchemy's ease of use, you can efficiently handle educational data. For more advanced features and enhancements, consider contributing to the project or extending its capabilities.
```