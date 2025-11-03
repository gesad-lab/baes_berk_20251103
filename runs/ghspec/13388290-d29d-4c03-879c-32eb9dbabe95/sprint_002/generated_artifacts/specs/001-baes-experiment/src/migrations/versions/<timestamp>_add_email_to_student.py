```python
from datetime import datetime
from sqlalchemy import Column, String
from flask_migrate import Migrate, Migration
from app import db

# Initialize migration
migration = Migration()

# Define the upgrade function to add the email column to the students table
def upgrade():
    """Add email column to the students table."""
    with db.engine.connect() as connection:
        with connection.begin():
            # Add email column only if it doesn't exist to avoid errors
            if not Column('email', String, nullable=False) in db.metadata.tables['students'].columns:
                connection.execute('ALTER TABLE students ADD COLUMN email VARCHAR NOT NULL')

# Define the downgrade function to remove the email column from the students table
def downgrade():
    """Remove email column from the students table."""
    with db.engine.connect() as connection:
        with connection.begin():
            # Note: Direct removal of columns in SQLAlchemy is not straightforward;
            # instead we typically recreate the table or handle differently as needed.
            raise NotImplementedError("Downgrade path to remove email column is not implemented.")

# This script will include a timestamp in the filename when invoked
if __name__ == "__main__":
    # You can implement logging here to record migration execution steps in the future
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f'migrations/versions/{timestamp}_add_email_to_student.py'
    with open(filename, 'w') as file:
        file.write(__file__)
```