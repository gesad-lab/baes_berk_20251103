from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migration, Migrate
from your_application import app, db  # Update the import based on your application structure

# Initialize migration support
migrate = Migrate(app, db)

class Teacher(db.Model):
    """Model representing a teacher in the system."""
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

def upgrade():
    """Run migration to add the teachers table."""
    db.create_all()
    # Check if the teachers table exists and create it if not
    if not db.session.query(Teacher).count():
        db.create_all()

def downgrade():
    """Revert migration changes."""
    db.drop_all()  # This will drop the teachers table
