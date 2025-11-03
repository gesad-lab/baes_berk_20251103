```python
from flask import jsonify, request
from app import app, db
from app.models import Course, Teacher

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  # New foreign key
    # other fields...

@app.route('/courses/<int:course_id>/teachers', methods=['POST'])
def associate_teacher_with_course(course_id):
    """Associate a teacher with a course."""
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Check if the teacher exists
    if not Teacher.query.get(teacher_id):
        return jsonify({"error": {"code": "E002", "message": "The specified teacher does not exist."}}), 404

    # Get the course or return 404 if not found
    course = Course.query.get_or_404(course_id)
    course.teacher_id = teacher_id  # Assigning the teacher ID to the course
    db.session.commit()  # Commit changes to the database

    return jsonify({
        "message": "Teacher associated with course successfully.",
        "course": {
            "id": course.id,
            "teacher_id": course.teacher_id
        }
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_with_teacher(course_id):
    """Retrieve course details along with assigned teacher."""
    course = Course.query.get_or_404(course_id)  # Get course or return 404

    if course.teacher_id:  # Check if the course has an associated teacher
        teacher = Teacher.query.get(course.teacher_id)
        teacher_info = {
            "name": teacher.name,
            "email": teacher.email
        }
    else:
        teacher_info = None  # No teacher assigned to the course

    return jsonify({
        "id": course.id,
        "teacher": teacher_info
    }), 200
```