# File: migrations/202XXXXXX_add_teacher_relationship.py

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from db.database import Base

class MigrationAddTeacherRelationship:
    """
    Migration script to alter the courses table to include a relationship 
    with the teachers table by adding the teacher_id foreign key.
    """

    def upgrade(self):
        """
        Apply the migration to add the teacher_id column and foreign key 
        constraint to the courses table.
        """
        with engine.connect() as connection:
            connection.execute("""
            ALTER TABLE courses
            ADD COLUMN teacher_id INTEGER,
            ADD FOREIGN KEY (teacher_id) REFERENCES teachers(id);
            """)
            print("Migration applied: Added teacher relationship to courses.")

    def downgrade(self):
        """
        Revert the migration by removing the teacher_id column and foreign key
        constraint from the courses table.
        """
        with engine.connect() as connection:
            connection.execute("""
            ALTER TABLE courses
            DROP COLUMN teacher_id;
            """)
            print("Migration reverted: Removed teacher relationship from courses.")

# Ensure the Base class is imported for migrations
Base.metadata.create_all(bind=engine)  # This might be in a separate context, adjust if necessary based on the framework setup.