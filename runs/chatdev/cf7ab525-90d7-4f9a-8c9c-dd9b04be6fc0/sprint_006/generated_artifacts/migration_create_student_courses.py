'''
Migration script to create the student_courses association table.
'''
from sqlalchemy import Column, Integer, ForeignKey, Table
from alembic import op
def upgrade():
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    op.drop_table('student_courses')