from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Student model for the database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create database schema at startup
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students/', methods=['GET'])
def get_all_students():
    """
    Retrieve all students from the database.

    Returns:
        JSON array of all students, each containing id and name.
        If no students are found, returns an empty list.
    """
    try:
        students = Student.query.all()
        # Convert student objects into a list of dictionaries
        students_list = [{"id": student.id, "name": student.name} for student in students]
        return jsonify(students_list), 200  # Return the list of students with HTTP 200 OK
    except Exception as e:
        # Log the exception for debugging (logging not shown in this snippet)
        return jsonify({"error": {"code": "E500", "message": "An error occurred while retrieving students."}}), 500

if __name__ == '__main__':
    app.run(debug=True)