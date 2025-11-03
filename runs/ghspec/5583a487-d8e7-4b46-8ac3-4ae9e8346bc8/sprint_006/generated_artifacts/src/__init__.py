from flask import Flask
from flask_migrate import Migrate
from app import db

app = Flask(__name__)

# Initialize migrations
migrate = Migrate(app, db)

@app.before_first_request
def run_migrations():
    """Run the database migrations on application startup."""
    with app.app_context():
        try:
            # This will apply any pending migrations
            from flask_migrate import upgrade
            upgrade()
            print("Migrations applied successfully.")
        except Exception as e:
            # Log the exception for debugging without revealing sensitive data
            app.logger.error(f"Error applying migrations: {e}")
            raise RuntimeError("Failed to apply database migrations") from e

# Other app configuration and routes would be set up here

if __name__ == "__main__":
    app.run()