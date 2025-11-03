# models/enrollment.py

from app import db

class Enrollment(db.Model):
    """
    Enrollment entity model that maps to the enrollments table in the database.
    
    Attributes:
        id (int): Unique identifier for the enrollment.
        student_id (int): The ID of the student being enrolled.
        course_id (int): The ID of the course the student is enrolled in.
    """
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    # Define relationships for easier access
    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"