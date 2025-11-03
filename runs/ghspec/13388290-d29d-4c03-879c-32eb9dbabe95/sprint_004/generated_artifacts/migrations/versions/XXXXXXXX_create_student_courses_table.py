from flask_migrate import Migration
from app import db
from app.models import StudentCourses

class Migration(Migration):
    """Migration script to create the StudentCourses junction table."""

    def upgrade(self):
        """Create the StudentCourses table for many-to-many relationship."""
        # Create the junction table to link students and courses
        db.create_table(
            'student_courses',
            db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
            db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
        )
    
    def downgrade(self):
        """Drop the StudentCourses table if rollback is needed."""
        db.drop_table('student_courses')