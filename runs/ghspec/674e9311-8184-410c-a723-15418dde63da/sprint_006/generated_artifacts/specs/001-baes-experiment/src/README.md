# README.md

# Project Title

## Introduction
This project is a web application that manages courses and teachers. It enables users to create, update, and view courses, as well as manage teacher assignments.

## Project Structure
```
src/
├── api.py                # Main API module
├── models/
│   ├── __init__.py      
│   ├── course.py         # Course model definition
│   └── teacher.py        # Teacher model definition
└── services/             # Service layer for business logic
tests/
├── __init__.py          
└── test_teacher.py       # Unit tests for teacher functionalities
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database (ensure you have the relevant database server running):
   ```bash
   # Run migrations to set up the initial database schema
   alembic upgrade head
   ```

## Usage
- Start the application:
  ```bash
  flask run
  ```

- The API endpoints include:
  - **Courses**
    - `POST /courses`: Create a new course
    - `GET /courses/<courseId>`: Retrieve a specific course (including assigned teacher)
    - `PUT /courses/<courseId>/assign-teacher`: Assign a teacher to the course

## Database Schema Changes
### Course Model
The `Course` entity has been updated to include a foreign key relationship with the `Teacher` model. Each course can have an optional teacher assigned to it.

Example:
```python
class Course(Base):
    """Model representing a Course with an optional associated Teacher."""
    
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")
```

### Migrations
Use Alembic to manage schema migrations. The latest migration includes adding the `teacher_id` column to the `courses` table.

## Running Tests
Run the unit tests to ensure everything is working as expected:
```bash
pytest tests/
```

## Contributing
We welcome contributions to enhance the project. Please open an issue or submit a pull request for any improvements or feature requests. 

## License
This project is licensed under the MIT License - see the LICENSE file for details.