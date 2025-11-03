```python
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.database import migrate_database
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_first_request
def initialize():
    """Initialize the database and perform any necessary migrations."""
    migrate_database()

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the application's status.

    Returns:
        JSON response indicating the application health status.
    """
    try:
        # Attempt to query the database to ensure connectivity
        db.session.query('1').from_statement('SELECT 1').all()
        return jsonify({"status": "Healthy"}), 200
    except Exception as e:
        return jsonify({"status": "Unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```