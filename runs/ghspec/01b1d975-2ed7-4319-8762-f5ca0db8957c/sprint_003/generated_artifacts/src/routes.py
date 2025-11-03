```python
# src/routes.py

from flask import Flask, request, jsonify
from src.controllers import create_course, get_courses

app = Flask(__name__)

@app.route('/courses', methods=['POST'])
def add_course():
    """Create a new course based on the provided JSON data.

    Returns:
        Response: JSON response with the created course data or error details.
    """
    return create_course(request.json)

@app.route('/courses', methods=['GET'])
def retrieve_courses():
    """Retrieve all existing courses.

    Returns:
        Response: JSON response with the list of courses or an error message.
    """
    return get_courses()
```