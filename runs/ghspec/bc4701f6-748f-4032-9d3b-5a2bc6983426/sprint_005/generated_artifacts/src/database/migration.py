```python
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, Table

# Define the database URL here (example: "sqlite:///./test.db")
DATABASE_URL = "your_database_url_here"

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)
metadata = MetaData()

def upgrade():
    """Create Teacher table within the existing database."""
    # Define the Teacher table
    teacher_table = Table(
        'Teacher', metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, unique=True, nullable=False),
    )

    # Create the Teacher table if it doesn't exist
    metadata.create_all(engine)

def downgrade():
    """Drop the Teacher table if it exists."""
    # Define the Teacher table for dropping
    teacher_table = Table('Teacher', metadata, autoload_with=engine)
    
    # Drop the Teacher table
    teacher_table.drop(engine)

# Run the upgrade function to apply changes on application startup
if __name__ == "__main__":
    upgrade()
```