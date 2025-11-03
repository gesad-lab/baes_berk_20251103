'''
Main entry point for the application.
'''
from database import create_database
from migration import migrate
if __name__ == "__main__":
    migrate()  # Ensure migration is applied
    create_database()  # Ensure this is called only when necessary
    import gui  # Import GUI after migration and database creation