from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    """Student model representing a student entity."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student from the database.
    
    Args:
        student_id (int): The unique identifier of the student to be deleted.
    
    Returns:
        JSON response with success or error message and appropriate HTTP status code.
    """
    try:
        student = Student.query.get(student_id)
        if student is None:
            return jsonify({"error": {"code": "E404", "message": "Student not found."}}), 404
        
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted successfully."}), 200
    
    except SQLAlchemyError as e:
        # Log the error for debugging (not shown here for brevity)
        return jsonify({"error": {"code": "E500", "message": "Internal server error."}}), 500

# Initialize the database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates the database tables if they don't exist
    app.run(debug=True)