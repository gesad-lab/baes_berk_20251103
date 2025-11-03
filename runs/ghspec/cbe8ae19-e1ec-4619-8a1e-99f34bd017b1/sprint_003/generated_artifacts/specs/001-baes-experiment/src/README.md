# README.md

# Project Title

## Overview
This project is designed to manage students and courses in an educational setting. It utilizes a microservice architecture and follows the principles of RESTful API design.

## Project Setup
To set up the project, follow these instructions:

1. **Clone the Repository**:
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Set Up a Virtual Environment**:
   Ensure you have Python installed, then create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the necessary packages using the `requirements.txt` file. Make sure it reflects the current dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Data Model
### Course Model
The `Course` model represents a course entity with the following attributes:
- `id`: Unique identifier for the course
- `name`: The name of the course
- `level`: The educational level of the course

You can find the model implementation in `models/course.py`.

## Database Migration
To add the `courses` table without impacting existing `students` data, a migration script has been created. You can apply migrations as follows:
1. Ensure your application is running:
   ```bash
   python app.py
   ```

2. Run the migration command:
   ```bash
   python manage.py db upgrade
   ```

### Example Migration Script
The migration script adds the new `courses` table while preserving existing data.
```python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import db, Course

# Initialize migration
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Create tables
def upgrade():
    db.create_all()

def downgrade():
    db.drop_all()
```

## Service Layer
The service layer for managing courses and related functionalities is located in `services/course_service.py`. It includes:
- **Create Course**: Functionality to create a new course
- **Fetch Course**: Functionality to retrieve course details
- **List Courses**: Functionality to retrieve all courses with appropriate validation

## API Layer
The API layer has been updated to include endpoints for managing courses. You can create and retrieve courses via the following endpoints:
- **POST /api/courses**: Create a new course
- **GET /api/courses**: List all courses
- **GET /api/courses/<course_id>**: Retrieve a specific course

## Testing
Please ensure adequate unit tests have been written for the course functionalities. The tests can be located in `tests/test_course_service.py`. Each service and API route should comply with a minimum coverage of 70%.

## Error Handling
Input validation has been implemented to ensure that course names and levels are valid strings and not empty. If an invalid input is detected, an appropriate error message will be returned.

## Conclusion
This project is a foundational step in building a comprehensive educational management system. For any issues or contributions, please refer to the contributing section.