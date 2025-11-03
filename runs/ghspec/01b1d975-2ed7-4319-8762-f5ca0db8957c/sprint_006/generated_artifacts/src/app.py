```python
from flask import Flask
from src.models import db  # Assuming db is initialized with SQLAlchemy

def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)

    if config is not None:
        app.config.update(config)

    # Initialize the database
    db.init_app(app)

    # Run all migrations when the app starts
    with app.app_context():
        from src.migrations import run_migrations  # Assuming there is a function to handle migrations
        run_migrations()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
```