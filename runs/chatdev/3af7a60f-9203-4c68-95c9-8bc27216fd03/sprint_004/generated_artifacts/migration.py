'''
Migration script to add courses table to the database.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    # Create student_courses association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )
    # Migrate existing data
    connection = op.get_bind()
    existing_students = connection.execute("SELECT id FROM students").fetchall()
    existing_courses = connection.execute("SELECT id FROM courses").fetchall()
    # Example logic to determine courses for a student
    # This is a placeholder; replace with actual logic
    for student in existing_students:
        # Assuming a logic to determine which courses a student is enrolled in
        # This is a placeholder; replace with actual logic
        courses_for_student = []  # Fetch or determine the courses for this student
        for course_id in courses_for_student:
            connection.execute(
                "INSERT INTO student_courses (student_id, course_id) VALUES (:student_id, :course_id)",
                {"student_id": student.id, "course_id": course_id}
            )
def downgrade():
    op.drop_table('student_courses')  # Remove the association table
    op.drop_table('courses')  # Remove courses table