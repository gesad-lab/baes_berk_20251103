"""Add email field to Student and create Course table
Revision ID: <revision_id>
Revises: <previous_revision_id>
Create Date: <date>
"""
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, you can set a default value for existing records
    op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # Alter the column to make it non-nullable
    op.alter_column('students', 'email', nullable=False)
    # Create Course table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Create the association table for many-to-many relationship
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_column('students', 'email')