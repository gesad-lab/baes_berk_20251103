from flask import Flask, jsonify, request
from models import Base, init_db
from routes import student_routes

app = Flask(__name__)

# Initialize the SQLite database and create the schema
@app.before_first_request
def initialize_database():
    init_db()

# Register API routes
app.register_blueprint(student_routes)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Student Management Application!"})

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development purposes
