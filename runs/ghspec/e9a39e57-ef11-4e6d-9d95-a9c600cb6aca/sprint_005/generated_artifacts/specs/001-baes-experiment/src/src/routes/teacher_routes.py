```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def upgrade():
    """Creates the teachers table in the database."""
    db.create_all(bind=None)  # This will create all tables, including teachers

def downgrade():
    """Drops the teachers table from the database."""
    db.drop_all(bind=None)  # This will drop all tables, including teachers
```