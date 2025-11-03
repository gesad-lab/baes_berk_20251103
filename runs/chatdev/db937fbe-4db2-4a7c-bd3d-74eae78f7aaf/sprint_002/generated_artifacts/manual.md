Here’s a detailed user manual for the ChatDev application, including installation instructions, main functions, and usage guidelines.

```markdown
# ChatDev Application

Changing the digital world through programming.

## Introduction

The ChatDev application is designed to manage student data efficiently. With the recent update, we have added an email field to the Student entity, allowing for better communication and data management. This application utilizes SQLAlchemy for database interactions and Pydantic for data validation.

## Main Functions

- **Student Management**: Create, read, update, and delete student records.
- **Email Field**: Each student now has an associated email address, which is required for creating a new student record.
- **Database Migration**: The application includes a migration script that updates the database schema without losing existing data.

## Quick Install

To get started with the ChatDev application, you need to install the required dependencies. You can do this using `pip`:

```bash
pip install -r requirements.txt
```

### Environment Setup

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd chatdev_app
   ```

2. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**: The application uses SQLite for database management. The database file `students.db` will be created automatically when you run the application for the first time.

## How to Use the Application

### Running the Application

To run the application, execute the following command:

```bash
python main.py
```

This command will create the necessary database tables and add the email column to the existing Student table if it does not already exist.

### Creating a New Student

To create a new student, you can use the `StudentCreate` schema defined in `schemas.py`. Here’s an example of how to create a new student:

```python
from schemas import StudentCreate
from database import get_db

# Example of creating a new student
new_student = StudentCreate(name="John Doe", email="john.doe@example.com")

# Save to database (pseudo-code)
db = next(get_db())
db.add(new_student)
db.commit()
```

### Retrieving Student Data

To retrieve student data, you can query the database using SQLAlchemy. Here’s a simple example:

```python
from models import Student
from database import get_db

# Example of retrieving all students
db = next(get_db())
students = db.query(Student).all()
for student in students:
    print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}")
```

### Updating Student Information

To update a student's information, you can fetch the student record, modify the fields, and save the changes:

```python
# Example of updating a student's email
student = db.query(Student).filter(Student.id == 1).first()
student.email = "new.email@example.com"
db.commit()
```

### Deleting a Student

To delete a student record, you can use the following code:

```python
# Example of deleting a student
student = db.query(Student).filter(Student.id == 1).first()
db.delete(student)
db.commit()
```

## Conclusion

The ChatDev application provides a robust framework for managing student data with the added functionality of email management. By following the instructions above, you can set up the environment, run the application, and manage student records effectively.

For further assistance or inquiries, please contact our support team.
```

This manual provides a comprehensive overview of the ChatDev application, ensuring users can easily understand and utilize its features.