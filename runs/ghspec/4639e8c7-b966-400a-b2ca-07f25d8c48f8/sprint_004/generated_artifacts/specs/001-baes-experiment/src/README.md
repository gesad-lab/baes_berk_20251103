# README.md

# Student Management Web Application

This application provides functionalities to manage student records and courses effectively, including the creation, retrieval, and updating of course details. Additionally, this version includes features to manage student-course associations.

## Features

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records.
- **Student-Course Association**: Link students to courses, enabling better tracking of student enrollment and progress.

## Project Structure

The project structure is as follows:

```
student_management/
├── src/
│   ├── app.py               # Main application file (update logic for associations here)
│   ├── models.py            # New StudentCourse model defined here
│   ├── routes.py            # Updated to include student-course association endpoints
│   ├── services.py          # Logic for handling student-course associations
│   └── db.py                # Migration scripts for join table
├── tests/
│   ├── test_routes.py       # New tests for student-course association endpoints
│   └── test_services.py     # Tests covering student-course business logic
├── requirements.txt          # Updated to reflect any new dependencies
└── README.md                 # Updated documentation for new features
```

## User Scenarios & Testing

1. **As an Admin User**, I want to create a new course record with a name and level so that I can manage course offerings effectively.
2. **As an Admin User**, I want to link students to courses so that I can track which courses students are enrolled in and monitor their progress.
3. **As a User**, I want to retrieve details of courses a student is enrolled in, providing clear visibility into their academic journey.

## Technology Stack

- **Language**: Python 3.11+
- **Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest
- **Documentation**: Markdown

## Installation

To install the project dependencies, run:

```
pip install -r requirements.txt
```

## Running the Application

To run the application, execute:

```
python src/app.py
```

## Running Tests

To run the tests using pytest, execute:

```
pytest
```

This will discover and run the tests in the `tests` folder. Make sure to keep the testing environment isolated from the production database.