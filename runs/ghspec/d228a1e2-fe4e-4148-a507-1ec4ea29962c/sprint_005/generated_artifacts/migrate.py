```python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# This function sets up the teacher migration using Flask-Migrate.
# It adds a new 'teachers' table with the specified fields while 
# ensuring existing data in other tables remains unaffected.
if __name__ == "__main__":
    manager.run()

# Define the migration for the Teacher entity
def create_teachers_table():
    """Create teachers table in the database."""
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.orm import relationship

    class Teacher(db.Model):
        """Model for the Teacher entity."""
        __tablename__ = 'teachers'
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)

        # Optionally, define relationships if needed
        # courses = relationship('Course', back_populates='teacher')

    # The migration logic will be called here to apply the new table structure
    db.create_all()

# Execute the migration when the script is run
create_teachers_table()
```