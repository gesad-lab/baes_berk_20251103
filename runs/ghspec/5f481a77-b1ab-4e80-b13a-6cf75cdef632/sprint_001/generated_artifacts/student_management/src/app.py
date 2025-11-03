import os
from flask import Flask
from config import Config
from db import initialize_database

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database schema on application startup
initialize_database()

# Rest of the API endpoints will be defined here
@app.route('/students', methods=['POST'])
def create_student():
    pass  # Implementation for creating a student

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    pass  # Implementation for retrieving a student by ID

if __name__ == '__main__':
    app.run()