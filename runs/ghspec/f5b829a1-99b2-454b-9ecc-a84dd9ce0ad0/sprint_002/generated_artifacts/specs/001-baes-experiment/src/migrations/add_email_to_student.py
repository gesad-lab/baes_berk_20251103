from sqlalchemy import Column, String, Integer
from src.models import Base

class Migration_AddEmailToStudent(Base):
    """Migration to add the email field to the Student entity"""
    
    __tablename__ = "students"  # Targeting the existing Student table

    # Adding the new email column to the existing table
    email = Column(String, nullable=False)  # Specify the email field with non-null constraint

    def upgrade(self):
        """Apply the migration to add the email field to the students table."""
        # Create the email column in the existing students table
        op.add_column("students", sa.Column("email", sa.String(), nullable=False))

    def downgrade(self):
        """Revert the migration by removing the email field from the students table."""
        # Remove the email column if the migration is rolled back
        op.drop_column("students", "email")