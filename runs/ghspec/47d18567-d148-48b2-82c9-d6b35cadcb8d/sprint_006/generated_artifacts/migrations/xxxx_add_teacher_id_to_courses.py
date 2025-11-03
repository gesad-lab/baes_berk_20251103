"""Add teacher_id to courses table

Revision ID: 1234567890ab
Revises: previous_revision_id
Create Date: 2023-10-01 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    """
    Upgrade the database schema to add a teacher_id column to the courses table.
    This column references the id column in the teachers table and allows for NULL values.
    This ensures that existing records remain intact during the migration.
    """
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    """
    Downgrade the database schema by removing the teacher_id column from the courses table.
    This reverts the database schema to its previous state before the upgrade.
    """
    op.drop_column('courses', 'teacher_id')