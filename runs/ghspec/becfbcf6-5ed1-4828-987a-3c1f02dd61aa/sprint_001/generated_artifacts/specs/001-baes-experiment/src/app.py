```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.before_first_request
def create_tables():
    """Creates the database tables if they do not exist."""
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Creates a new student with the provided name."""
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "The name field is required."}}), 400
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieves the list of all students."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

if __name__ == '__main__':
    app.run(debug=True)
```
```dockerfile
# Dockerfile

# Start from the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for the SQLite database
ENV DATABASE_URI=sqlite:///students.db

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
```