'''
Migration script to add teacher_id to Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_teacher_relationship_to_courses'
down_revision = 'add_teacher_table'  # Ensure this is the correct previous revision
branch_labels = None
depends_on = None
def upgrade():
    # Add teacher_id column to courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])
def downgrade():
    # Drop the foreign key and the column if downgrading
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')