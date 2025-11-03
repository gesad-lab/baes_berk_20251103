'''
Handles the database migration for adding the student_course association table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    op.create_table('student_course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
def downgrade():
    op.drop_table('student_course')