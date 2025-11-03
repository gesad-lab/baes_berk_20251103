```python
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Course(db.Model):
    """Course model representing an educational offering."""
    
    __tablename__ = 'course'
    
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String, nullable=False)    # Course name (required)
    level = db.Column(db.String, nullable=False)   # Course level (required)

def upgrade():
    """Create the Course table in the database."""
    op.create_table(
        'course',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    """Drop the Course table from the database."""
    op.drop_table('course')
```