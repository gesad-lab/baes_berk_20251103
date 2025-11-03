from sqlalchemy import create_engine, Column, String, Table, MetaData
from alembic import op
import sqlalchemy as sa


# Migration to add the email column to the students table
def upgrade():
    # Fetch the current connection to the database
    connection = op.get_bind()
    metadata = MetaData(bind=connection)

    # Define the existing students table
    students_table = Table('students', metadata, autoload_with=connection)
    
    # Add the new email column with a NOT NULL constraint
    email_column = Column('email', String, nullable=False)
    email_column.create(students_table)

    # Ensure existing data remains intact could involve data transfer if needed,
    # but here we directly add the column as it's a migration step.


def downgrade():
    # Fetch the current connection to the database
    connection = op.get_bind()
    metadata = MetaData(bind=connection)

    # Define the existing students table for downgrade
    students_table = Table('students', metadata, autoload_with=connection)

    # Drop the email column if it exists
    email_column = students_table.c.email
    email_column.drop()