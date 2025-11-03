import sqlite3
import json
import logging
from flask import Flask, request, jsonify

# Initialize structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        conn.commit()
    logger.info("Database initialized and students table created.")

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    data = request.json
    if 'name' not in data:
        error_msg = {"error": {"code": "E001", "message": "Name is required to create a student."}}
        logger.error(f"Failed to create student: {json.dumps(error_msg)}")
        return jsonify(error_msg), 400

    name = data['name']
    age = data.get('age')

    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', (name, age))
        conn.commit()

    logger.info("Student created successfully", extra={"name": name, "age": age})
    return jsonify({"message": "Student created successfully."}), 201

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all student records."""
    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()

    logger.info("Retrieved student records.", extra={"count": len(students)})
    return jsonify(students), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)