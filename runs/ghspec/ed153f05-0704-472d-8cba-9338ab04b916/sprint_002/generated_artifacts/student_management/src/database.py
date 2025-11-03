```python
from src.database import db

def upgrade():
    """Add email column to students table."""
    with db.engine.begin() as connection:
        # Add the email column with default value NULL
        connection.execute("""
            ALTER TABLE students
            ADD COLUMN email VARCHAR(255) UNIQUE
        """)

def downgrade():
    """Remove email column from students table."""
    with db.engine.begin() as connection:
        # Drop the email column if it exists
        connection.execute("""
            ALTER TABLE students
            DROP COLUMN email
        """)

if __name__ == "__main__":
    print("Run this script using a migration tool, not directly.")
```