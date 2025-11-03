"""add_email_to_student_table

Revision ID: 20231030_add_email_to_student_table
Revises: previous_revision_id
Create Date: 2023-10-30
"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Add 'email' column to the 'student' table with a default value."""
    # Adding new column 'email' to the 'student' table
    op.add_column('student', sa.Column('email', sa.String(), nullable=False, server_default=''))


def downgrade():
    """Remove 'email' column from the 'student' table."""
    # Dropping 'email' column from the 'student' table
    op.drop_column('student', 'email')