'''
Migration script to add Course table and relationship.
'''
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
# revision identifiers, used by Alembic.
revision = '20231001_add_course_table'  # Update with a unique revision ID
down_revision = None  # Update with the last migration revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # Create the student_courses association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
    # Logic to migrate existing relationships (if applicable)
    # Assuming there is a way to determine existing relationships
    # This is a placeholder; you will need to adjust based on your existing schema
    existing_relationships = op.get_bind().execute(text("SELECT student_id, course_id FROM existing_relationships"))
    for student_id, course_id in existing_relationships:
        op.execute(
            "INSERT INTO student_courses (student_id, course_id) VALUES (:student_id, :course_id)",
            {"student_id": student_id, "course_id": course_id}
        )
def downgrade():
    op.drop_table('student_courses')
    op.drop_table('courses')