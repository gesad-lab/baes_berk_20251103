# File: src/database.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

class StudentCourse(db.Model):
    """Model to link Students and Courses in a many-to-many relationship."""
    __tablename__ = 'student_courses'
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

def migrate_database():
    """Function to handle database migration for the student_courses table."""
    # Check if the 'student_courses' table already exists to avoid re-creating it
    if not db.engine.dialect.has_table(db.engine, 'student_courses'):
        # Create the 'student_courses' table
        db.create_all(bind='student_courses')
        
        # Log that the migration has been performed
        print("Migration completed: 'student_courses' table created.")
    else:
        print("'student_courses' table already exists. Migration skipped.")
        
    # Ensure to handle exceptions and log them accordingly
    try:
        # Migration logic to be executed here
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Migration failed: {str(e)}")  # Log the error for debugging purposes
```