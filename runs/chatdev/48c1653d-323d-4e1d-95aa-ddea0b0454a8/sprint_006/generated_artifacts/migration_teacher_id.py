'''
Migration script to add teacher_id to Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_id_to_course'
down_revision = 'add_teacher_table'  # Updated to the last migration
branch_labels = None
depends_on = None
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))
def downgrade():
    op.drop_column('courses', 'teacher_id')