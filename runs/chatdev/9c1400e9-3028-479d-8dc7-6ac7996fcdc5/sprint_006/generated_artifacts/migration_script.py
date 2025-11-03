'''
Database migration script to add Teacher table and ensure email field is required in Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_relationship_to_courses'
down_revision = 'add_teacher_table'  # Ensure this is the correct previous migration
branch_labels = None
depends_on = None
def upgrade():
    # Add teacher_id column to courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    # Remove teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')