from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

    # Establish the relationship to Course through StudentCourse
    courses = db.relationship('StudentCourse', back_populates='student')


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String)

    # Establish the relationship to Student through StudentCourse
    students = db.relationship('StudentCourse', back_populates='course')


class StudentCourse(db.Model):
    __tablename__ = 'student_courses'

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True, nullable=False)

    # Establish relationship to Student and Course models
    student = db.relationship('Student', back_populates='courses')
    course = db.relationship('Course', back_populates='students')