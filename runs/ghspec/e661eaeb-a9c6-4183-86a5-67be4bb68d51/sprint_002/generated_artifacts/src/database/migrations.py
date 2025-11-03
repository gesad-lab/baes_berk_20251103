from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from alembic import op

def upgrade():
    """Add the email column to the students table."""
    with op.batch_alter_table("students") as batch_op:
        # Add the email column with a non-nullable constraint
        batch_op.add_column(Column("email", String, nullable=False))

def downgrade():
    """Remove the email column from the students table."""
    with op.batch_alter_table("students") as batch_op:
        # Drop the email column
        batch_op.drop_column("email")