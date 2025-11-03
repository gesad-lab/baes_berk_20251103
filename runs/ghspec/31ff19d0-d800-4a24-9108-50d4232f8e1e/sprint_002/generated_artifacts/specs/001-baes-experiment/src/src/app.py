from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Flask-Migrate and Manager
migrate = Migrate(app, db)
manager = Manager(app)

@manager.command
def migrate_db():
    """Run database migrations without data loss"""
    # Run migrations to add 'email' to the Student table
    migrate.upgrade()

if __name__ == '__main__':
    # Running the Flask app with the Manager
    manager.run()
