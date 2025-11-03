from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "sqlite:///./students.db"  # Update this according to your database configuration

def run_migration():
    """Run the database migration to add the email column to the students table."""
    engine = create_engine(DATABASE_URL)
    metadata = MetaData(bind=engine)

    # Reflect the existing database schema
    metadata.reflect()

    # Check if the students table exists
    if 'students' not in metadata.tables:
        print("The students table does not exist.")
        return

    # Get the students table
    students_table = Table('students', metadata, autoload_with=engine)

    # Check if the email column already exists
    if 'email' in students_table.columns:
        print("The email column already exists in the students table.")
        return

    # Start a migration transaction
    conn = engine.connect()
    trans = conn.begin()
    try:
        # Add the email column to the students table
        conn.execute(
            f'ALTER TABLE students ADD COLUMN email STRING NOT NULL'
        )
        trans.commit()
        print("Migration completed: email column added to students table.")
    except SQLAlchemyError as e:
        trans.rollback()
        print(f"Migration failed: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_migration()