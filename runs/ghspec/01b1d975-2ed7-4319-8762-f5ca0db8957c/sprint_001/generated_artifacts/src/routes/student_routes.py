```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    """Model for Student entity."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

@app.before_first_request
def create_tables():
    """Create database tables if they do not exist on application startup."""
    db.create_all()  # This method creates the database tables based on the models defined

if __name__ == '__main__':
    app.run(debug=True)
```