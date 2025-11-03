'''
Migration script to add Teacher table to the database.
'''
from sqlalchemy import create_engine, inspect, Column, String
from sqlalchemy.exc import NoSuchTableError
from models import Base
DATABASE_URL = "sqlite:///./students.db"
def upgrade():
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    inspector = inspect(engine)
    try:
        # Check if the 'teachers' table already exists
        if 'teachers' not in inspector.get_table_names():
            Base.metadata.create_all(engine)  # Create the Teacher table
        else:
            # Logic to check and alter the table if necessary
            columns = [column['name'] for column in inspector.get_columns('teachers')]
            if 'name' not in columns:
                # Add column logic here
                pass
            if 'email' not in columns:
                # Add column logic here
                pass
    except NoSuchTableError:
        print("Error: The 'teachers' table does not exist.")
    finally:
        connection.close()
if __name__ == "__main__":
    upgrade()