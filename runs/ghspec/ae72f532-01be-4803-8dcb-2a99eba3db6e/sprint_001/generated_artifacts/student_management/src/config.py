```python
from flask import Flask
from src.config import Config

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize other components here (e.g., database, blueprints)

    return app

if __name__ == "__main__":
    application = create_app()
    application.run(host='0.0.0.0', port=5000, debug=True)
```