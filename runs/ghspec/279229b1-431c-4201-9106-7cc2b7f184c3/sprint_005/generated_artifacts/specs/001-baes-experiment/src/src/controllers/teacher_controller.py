```python
# src/routes.py

from flask import Flask, request, jsonify
from src.controllers.teacher_controller import create_teacher  # Importing the teacher creation function

app = Flask(__name__)

# Define the POST /teachers endpoint
@app.route('/teachers', methods=['POST'])
def post_teacher():
    return create_teacher()

# Other existing routes...
```