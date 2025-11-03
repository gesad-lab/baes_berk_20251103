from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Student Model
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each student
    name = db.Column(db.String, nullable=False)  # Name of the student

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student(id={self.id}, name='{self.name}')>"

# Student Schema
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# Create the database and the student table if it doesn't exist
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoints and logic omitted for brevity

if __name__ == '__main__':
    app.run(debug=True)