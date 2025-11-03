```python
from flask import Flask, request, jsonify
from api.routes import student_routes

app = Flask(__name__)

# Register API routes
app.register_blueprint(student_routes)

@app.route('/')
def index():
    return "Welcome to the Student Management API."

if __name__ == '__main__':
    app.run(debug=True)
```