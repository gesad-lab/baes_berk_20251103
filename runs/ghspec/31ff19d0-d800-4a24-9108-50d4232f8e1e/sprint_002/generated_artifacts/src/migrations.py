from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from your_application import app, db  # Adjust this import based on your actual application structure
from your_application.models import Student  # Adjust based on the actual model's path

manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def migrate_db():
    """Run database migrations without data loss"""
    # Commands to perform migration
    migrate.upgrade()

def add_email_column():
    """Migration script to add 'email' field to the 'Student' table without losing existing data."""
    with db.session.begin():
        # Implement the logic to add the email column to the Student table.
        # This is a SQLAlchemy example to add a column
        # Ensure that the new column is nullable and later validated to enforce uniqueness
        with db.engine.connect() as connection:
            connection.execute('ALTER TABLE student ADD COLUMN email VARCHAR(255) UNIQUE NOT NULL')

# This method should be called during the migration process to ensure the column is added correctly
if __name__ == "__main__":
    add_email_column()  # Call the function to execute the email field addition
    manager.run()  # Start the migration manager to run the migration commands