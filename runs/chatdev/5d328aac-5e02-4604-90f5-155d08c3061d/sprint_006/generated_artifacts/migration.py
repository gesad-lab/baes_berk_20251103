'''
Migration script to create courses table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_table'
down_revision = 'add_teacher_table'  # Reference the migration that creates the teachers table
branch_labels = None
depends_on = None
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')),  # Added foreign key for teacher
    )
def downgrade():
    op.drop_table('courses')