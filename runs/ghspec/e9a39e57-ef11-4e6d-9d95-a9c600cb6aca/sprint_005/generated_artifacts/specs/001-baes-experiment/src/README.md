# Updated README.md

# Project Title

## Description

This project is a Flask application designed to manage students and courses, now enhanced with teacher management functionality. The application uses SQLAlchemy for ORM and is structured to maintain clear separation of concerns.

## Setup & Configuration

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy the example environment file and edit configurations:
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with your database configuration and any other settings.

## Running the Application Locally

To run the development server:

```bash
export FLASK_APP=src
export FLASK_ENV=development
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### Students

- **Get all students**: `GET /students`
- **Create a student**: `POST /students`
  - **Request Body**: `{"name": "Student Name", "email": "student@example.com"}`
  
### Courses

- **Get all courses**: `GET /courses`
- **Create a course**: `POST /courses`
  - **Request Body**: `{"title": "Course Title", "description": "Course Description"}`

### Teachers

- **Get all teachers**: `GET /teachers`
- **Create a teacher**: `POST /teachers`
  - **Request Body**: `{"name": "Teacher Name", "email": "teacher@example.com"}`

## Database Migrations

Make sure to run migrations when updating your database schema. Use the following command:

```bash
flask db migrate -m "Add Teacher model"
flask db upgrade
```

## Testing

To run the tests, use the following command:

```bash
pytest
```

Make sure all tests pass before pushing your changes.

## Contribution

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.