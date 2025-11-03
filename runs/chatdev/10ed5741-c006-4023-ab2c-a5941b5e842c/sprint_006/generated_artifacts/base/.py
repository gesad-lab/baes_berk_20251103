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
def downgrade():
    # Drop the association table
    op.drop_table('student_courses')