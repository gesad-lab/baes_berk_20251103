from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, Migration
from your_application import db  # Adjust the import based on the actual application structure

# Initialize migration object
migrate = Migrate()

# Migration class to create the Teacher table
class Migration(Migration):
    """Migration to create the teachers table."""

    version = 'XXXX_create_teacher_table'

    def upgrade():
        # Create the teachers table
        db.create_table('teachers',
            db.Column('id', db.Integer, primary_key=True),
            db.Column('name', db.String, nullable=False),
            db.Column('email', db.String, nullable=False, unique=True)
        )

    def downgrade():
        # Drop the teachers table
        db.drop_table('teachers')