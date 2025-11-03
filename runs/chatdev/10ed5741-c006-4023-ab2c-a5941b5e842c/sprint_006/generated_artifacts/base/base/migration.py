'''
Migration script to add student_courses association table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_student_courses_table'
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Create the association table
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
    # Example logic to populate student_courses if there are existing relationships
    connection = op.get_bind()
    # Assuming you have a way to determine existing relationships
    # This is a placeholder; replace with actual logic to find existing relationships
    existing_relationships = connection.execute("SELECT student_id, course_id FROM existing_relationships")  
    for student_id, course_id in existing_relationships:
        connection.execute(
            "INSERT INTO student_courses (student_id, course_id) VALUES (:student_id, :course_id)",
            {"student_id": student_id, "course_id": course_id}
        )
def downgrade():
    # Drop the association table
    op.drop_table('student_courses')