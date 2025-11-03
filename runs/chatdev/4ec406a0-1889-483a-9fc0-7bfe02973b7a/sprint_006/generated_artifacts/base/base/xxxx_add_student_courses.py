'''
Migration script to add the student_courses association table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_add_student_courses'  # Example revision ID
down_revision = 'previous_revision_id'  # Replace with the actual last migration ID
branch_labels = None
depends_on = None
def upgrade():
    # Create the association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
def downgrade():
    # Drop the association table
    op.drop_table('student_courses')