from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # Example database URI
db = SQLAlchemy(app)

# Example models (assuming these are defined)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

class StudentCourse(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)

# Schema for validating request bodies
class AddCoursesSchema(Schema):
    course_ids = fields.List(fields.Int(), required=True)

# Define the endpoint for adding courses to a student
@app.route('/students/<int:id>/courses', methods=['POST'])
def add_courses(id):
    # Validate the request data
    try:
        data = request.get_json()
        validated_data = AddCoursesSchema().load(data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), 400

    course_ids = validated_data.get('course_ids')

    # Associate courses with the student
    for course_id in course_ids:
        try:
            student_course = StudentCourse(student_id=id, course_id=course_id)
            db.session.add(student_course)
        except IntegrityError:
            # Handle foreign key constraint violations (student or course not found)
            db.session.rollback()
            return jsonify({"error": {"code": "E002", "message": "Course or student not found"}}), 404

    # Commit the changes to the database
    db.session.commit()

    return jsonify({"message": "Courses added successfully"}), 200

# Example of retrieving courses for a student (implementing a placeholder)
@app.route('/students/<int:id>/courses', methods=['GET'])
def get_courses(id):
    # Implementation would be similar to the add_courses function
    # Retrieve and return courses associated with the student
    pass

# Run the application if this is the main module
if __name__ == '__main__':
    db.create_all()  # Ensure tables are created before running
    app.run(debug=True)  # Set debug to False in production environments